from fastapi import APIRouter, Request, Depends, Body
from fastapi.responses import RedirectResponse
import httpx
import os
from datetime import datetime, timedelta
from app.database import get_db
from app.core.auth import get_current_user
from pydantic import BaseModel
from app.models import Users
from app.config import settings

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
    supabase=Depends(get_db),
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
            expires_at = datetime.now() + timedelta(seconds=token_data["expires_in"])

            # Store tokens in Supabase
            supabase.table("ynab_tokens").upsert(
                {
                    "user_id": user.id,
                    "access_token": token_data["access_token"],
                    "refresh_token": token_data["refresh_token"],
                    "expires_at": expires_at.isoformat(),
                    "created_at": datetime.now().isoformat(),
                    "updated_at": datetime.now().isoformat(),
                }
            ).execute()

            # Redirect back to frontend with success message
            return RedirectResponse(
                url=f"{os.environ.get('FRONTEND_URL')}/settings?ynab_status=connected"
            )

    except httpx.HTTPStatusError as e:
        print(f"YNAB API error: {str(e)}")
        return RedirectResponse(
            url=f"{os.environ.get('FRONTEND_URL')}/settings?error=token_exchange_failed"
        )
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return RedirectResponse(
            url=f"{os.environ.get('FRONTEND_URL')}/settings?error=server_error"
        )
