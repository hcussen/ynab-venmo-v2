from typing import Optional
from fastapi import FastAPI, Form, Request
from pydantic_settings import BaseSettings, SettingsConfigDict
from supabase import create_client, Client
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Create logger
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


url: str = settings.supabase_url
key: str = settings.supabase_key
supabase: Client = create_client(url, key)


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
