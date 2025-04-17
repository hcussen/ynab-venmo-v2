from fastapi import APIRouter, Form, Request
from typing import Optional
import json
from datetime import datetime, timezone
from app.config import logger, supabase

router = APIRouter(
    prefix="/webhooks",
    tags=["webhooks"],
)

def save_copy_in_storage(email_json, slug: str):
    # Generate a unique filename using timestamp
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}.json"
    try:
        # Upload email data to Supabase storage in the emails/{slug} folder
        response = (
            supabase.storage
            .from_("emails")
            .upload(
                file=email_json.encode(),
                path=f"{slug}/{filename}",
                file_options={"cache-control": "3600", "upsert": "false"}
            )
        )
        logger.info(f"Email uploaded successfully to Supabase: {filename}")
        return {"status": "success", "message": "Email uploaded successfully", "filename": filename}
        
    except Exception as e:
        logger.error(f"Failed to upload email to Supabase: {str(e)}")
        return {"status": "error", "message": f"Failed to upload email: {str(e)}"}


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
    slug = to.split("@")[0]
    
    # Prepare email data
    email_data = {
        "subject": subject,
        "to": to,
        "from": from_,
        "text": text,
        "envelope": json.loads(envelope),
        "received_at": datetime.now(timezone.utc).isoformat(),
        "dump": str(request.__dict__)
    }
    
    # Convert email data to JSON string
    email_json = json.dumps(email_data)

    save_copy_in_storage(email_json, slug)    

    
    
    

