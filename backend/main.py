from fastapi import FastAPI, Form, Depends, Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import jwt
from jwt.exceptions import InvalidTokenError

import requests

from sqlalchemy.orm import Session

from typing import Optional

from app.config import settings, logger
from app.database import get_db
from app.models import Planets, Users

# set up the JWT verification key
jwt_response = requests.get(
    f"{settings.supabase_url}/rest/v1/?apikey={settings.supabase_key}"
)
jwt_secret = jwt_response.headers.get("x-jwt-secret")
print("hello")


app = FastAPI()
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    """
    Validate JWT token and return the user
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            settings.supabase_jwt_key,
            algorithms=["HS256"],
            audience="authenticated",
            options={"verify_signature": True},
        )

        user_id = payload.get("sub")
        email = payload.get("email")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )

        return Users(id=user_id, email=email)
    except InvalidTokenError as e:
        print(f"Token validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or expired token",
        )
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Server error: {str(e)}",
        )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/planets")
async def get_planets(db: Session = Depends(get_db)):
    planets = db.query(Planets).all()
    return planets


@app.get("/protected")
async def protected_route(current_user: Users = Depends(get_current_user)):
    return {
        "message": f"Hello, {current_user.email}! This is a protected route.",
        "user_id": current_user.id,
    }


@app.post("/parse")
async def sendgrid_inbound_webhook(
    request: Request,
    subject: str = Form(...),
):
    """
    Simple handler for SendGrid Parse webhook that just logs the email subject.
    This is useful for initial testing of the webhook configuration.
    """
    logger.info(f"Received email with subject: {subject}")

    return {"status": "success", "message": "Email subject logged successfully"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
