from typing import Optional
from fastapi import FastAPI, Form, Request
from app.config import settings, supabase, logger


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/supabase")
async def get_supabase():
    response = supabase.table("planets").select("*").execute()
    return response


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
