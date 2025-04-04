from fastapi import APIRouter

from app.api.routes import general, webhooks, ynab

api_router = APIRouter()

# Include all the router modules
api_router.include_router(general.router)
api_router.include_router(webhooks.router)
api_router.include_router(ynab.router)
