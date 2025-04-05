from fastapi import Depends, HTTPException
from datetime import datetime, timedelta, timezone
import httpx
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from app.database import get_db
from app.core.auth import get_current_user
from app.models import Users, Profiles
from app.config import settings


async def refresh_ynab_token(db: Session, profile: Profiles) -> str:
    """
    Refresh the YNAB access token using the stored refresh token.
    Returns the new access token and updates the database with new token information.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://app.ynab.com/oauth/token",
                data={
                    "client_id": settings.ynab_client_id,
                    "client_secret": settings.ynab_client_secret,
                    "grant_type": "refresh_token",
                    "refresh_token": profile.ynab_refresh_token,
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            response.raise_for_status()
            token_data = response.json()

            # Calculate new expiry time
            now_utc = datetime.now(timezone.utc)
            expires_at = now_utc + timedelta(seconds=token_data["expires_in"])

            # Update tokens in database
            values = {
                "id": profile.id,
                "ynab_access_token": token_data["access_token"],
                "ynab_refresh_token": token_data["refresh_token"],
                "ynab_token_expires_at": expires_at.isoformat(),
                "ynab_token_updated_at": now_utc.isoformat(),
            }
            update_values = {k: v for k, v in values.items() if k != "id"}

            statement = (
                insert(Profiles)
                .values(values)
                .on_conflict_do_update(index_elements=["id"], set_=update_values)
            )
            db.execute(statement)
            db.commit()

            return token_data["access_token"]

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=401,
            detail="Failed to refresh YNAB token. Please reconnect your YNAB account.",
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Internal server error while refreshing YNAB token"
        )


async def get_valid_ynab_token(
    db: Session = Depends(get_db), user: Users = Depends(get_current_user)
) -> str:
    """
    FastAPI dependency that ensures a valid YNAB token is available.
    Automatically refreshes the token if it's expired or about to expire.
    Returns the valid access token.
    """
    # Get user's profile
    profile = db.query(Profiles).filter(Profiles.id == user.id).first()
    if not profile or not profile.ynab_access_token:
        raise HTTPException(status_code=401, detail="YNAB account not connected")

    # Check if token is expired or about to expire (within 5 minutes)
    now_utc = datetime.now(timezone.utc)
    expires_at = profile.ynab_token_expires_at

    if expires_at - timedelta(minutes=5) <= now_utc:
        # Token is expired or about to expire, refresh it
        return await refresh_ynab_token(db, profile)

    return profile.ynab_access_token
