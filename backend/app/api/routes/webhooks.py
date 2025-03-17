from fastapi import APIRouter, Form, Request

from app.config import logger

router = APIRouter(
    prefix="/webhooks",
    tags=["webhooks"],
)


@router.post("/parse", summary="SendGrid inbound webhook")
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
