from fastapi import FastAPI
from app.api import api_router

# Create the FastAPI app
app = FastAPI(
    title="Your API",
    description="Your API description",
    version="0.1.0",
)


# Add a simple root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Include all API routes
app.include_router(api_router)
