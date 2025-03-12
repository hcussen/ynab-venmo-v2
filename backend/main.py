from typing import Optional
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

import os
from supabase import create_client, Client

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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
