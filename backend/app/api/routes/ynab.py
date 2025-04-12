from fastapi import APIRouter, Request, Depends, Body, HTTPException
from fastapi.responses import RedirectResponse
import httpx
import os
from datetime import datetime, timezone, timedelta
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.dialects.postgresql import insert
from pydantic import BaseModel

from app.core.auth import get_current_user
from app.core.ynab import get_valid_ynab_token
from app.database import get_db
from app.config import settings
from app.models import Users, Profiles

import random
import string

def generate_email_slug(email: str) -> str:
    email_prefix = email.split('@')[0][:5]  # Take up to first 5 chars of email
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))  # 5 random chars
    return f"{email_prefix}.{random_suffix}"

router = APIRouter(
    prefix="",
    tags=["ynab"],
)


class OAuthCallback(BaseModel):
    code: str


@router.post("/oauth/callback")
async def oauth_callback(
    request: Request,
    data: OAuthCallback,
    error: str = None,
    db=Depends(get_db),
    user: Users = Depends(get_current_user),
):
    print("code: ", data.code)
    code = data.code
    print("user_id: ", user.id)

    # Handle error from OAuth provider
    if error:
        return RedirectResponse(
            url=f"{os.environ.get('FRONTEND_URL')}/settings?error={error}"
        )

    # Ensure code is provided
    if not code:
        return RedirectResponse(
            url=f"{os.environ.get('FRONTEND_URL')}/settings?error=missing_code"
        )

    try:
        # Exchange code for token
        async with httpx.AsyncClient() as client:
            print("1")
            response = await client.post(
                "https://app.ynab.com/oauth/token",
                params={
                    "client_id": settings.ynab_client_id,
                    "client_secret": settings.ynab_client_secret,
                    "redirect_uri": settings.ynab_redirect_uri,
                    "grant_type": "authorization_code",
                    "code": code,
                },
                data={
                    "client_id": settings.ynab_client_id,
                    "client_secret": settings.ynab_client_secret,
                    "redirect_uri": settings.ynab_redirect_uri,
                    "grant_type": "authorization_code",
                    "code": code,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            print(response)
            response.raise_for_status()
            token_data = response.json()
            print(token_data)

            # Calculate expiry time
            now_utc = datetime.now(timezone.utc)

            expires_at = now_utc + timedelta(seconds=token_data["expires_in"])
            

            # Store tokens in Supabase
            values = {
                "id": user.id,
                "email_slug": generate_email_slug(user.email),
                "ynab_access_token": token_data["access_token"],
                "ynab_refresh_token": token_data["refresh_token"],
                "ynab_token_expires_at": expires_at.isoformat(),
                "ynab_token_created_at": now_utc.isoformat(),
                "ynab_token_updated_at": now_utc.isoformat(),
            }
            update_values = {k: v for k, v in values.items() if k != "id"}
            print(values)
            statement = (
                insert(Profiles)
                .values(values)
                .on_conflict_do_update(index_elements=["id"], set_=update_values)
            )
            print(statement)
            db.execute(statement)
            db.commit()

            # Redirect back to frontend with success message
            return {"success": True, "state": "Successfully exhanged token"}

    except httpx.HTTPStatusError as e:
        print(f"YNAB API error: {str(e)}")
        return {"success": False, "error": "YNAB API error", "message": e}
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return {"success": False, "error": "Server error", "message": e}


@router.get("/budgets")
async def get_budgets(
    token: str = Depends(get_valid_ynab_token) #this depends on get_urrent_user, so it's handling auth
):
    """Get all budgets for the authenticated user"""
    print("recived request to budgets")
    try:
        async with YNABClient(token) as client:
            budgets = await client.get_budgets()
            return budgets
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )