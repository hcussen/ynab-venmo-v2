from pydantic_settings import BaseSettings, SettingsConfigDict
from supabase import create_client, Client
import logging


class Settings(BaseSettings):
    # Supabase settings from your existing code
    supabase_url: str
    supabase_key: str
    supabase_pwd: str
    supabase_jwt_key: str

    # Add database URL for SQLAlchemy
    # This URL will point to your Supabase PostgreSQL database
    database_url: str

    # You can add other settings as needed
    env_name: str = "dev"

    model_config = SettingsConfigDict(env_file=".env")


# Create settings instance
settings = Settings()

# Create Supabase client
supabase: Client = create_client(settings.supabase_url, settings.supabase_key)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)
