from typing import Optional
from fastapi import FastAPI, Form, Depends, Request, HTTPException
from sqlalchemy.orm import Session

from app.config import logger
from app.database import get_db
from app.models import Planets


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/planets")
async def get_planets(db: Session = Depends(get_db)):
    planets = db.query(Planets).all()
    return planets


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
