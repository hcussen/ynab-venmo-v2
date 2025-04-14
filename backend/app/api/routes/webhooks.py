from fastapi import APIRouter, Form, Request
from typing import Optional
import json
from datetime import datetime, timezone
from app.config import logger, supabase

router = APIRouter(
    prefix="/webhooks",
    tags=["webhooks"],
)


@router.post("/parse", summary="SendGrid inbound webhook")
async def sendgrid_inbound_webhook(
    request: Request,
    subject: str = Form(...),
    to: str = Form(...),
    from_: str = Form(..., alias="from"),
    text: str = Form(...),
    html: str = Form(...),
    envelope: str = Form(...),
):
 
    """
    Handler for SendGrid Parse webhook that uploads the email content to Supabase.
    """
    logger.info(f"Received email with subject: {subject} from {from_}")

    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
    filename = f'request_data_{timestamp}.txt'
    with open(filename, 'w') as f:
        f.write(str(request.__dict__))
    logger.info(f"Request data saved to {filename}")
    
    with open(f'selected_request_data_{timestamp}.txt', 'w') as f:
        f.write("subject: " + subject + "\n")
        f.write("to: " + to + "\n")
        f.write("from: " + from_ + "\n")
        f.write("text: " + text + "\n")
        f.write("envelope: " + envelope + "\n")
    logger.info(f"Selected request data saved to selected_request_data_{timestamp}.txt")
    
    
    # Prepare email data
    email_data = {
        "subject": subject,
        "to": to,
        "from": from_,
        "text": text,
        "envelope": json.loads(envelope),
        "received_at": datetime.now(timezone.utc).isoformat()
    }
    
    # Generate a unique filename using timestamp
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"{to}_{timestamp}.json"
    
    try:
        # Upload email data to Supabase storage
        response = (
            supabase.storage
            .from_("emails")
            .upload(
                file=email_json.encode(),
                path=filename,
                file_options={"cache-control": "3600", "upsert": "false"}
            )
        )
        logger.info(f"Email uploaded successfully to Supabase: {filename}")
        return {"status": "success", "message": "Email uploaded successfully", "filename": filename}
        
    except Exception as e:
        logger.error(f"Failed to upload email to Supabase: {str(e)}")
        return {"status": "error", "message": f"Failed to upload email: {str(e)}"}

