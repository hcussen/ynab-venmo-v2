from fastapi import APIRouter, Depends
from typing import Optional
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.database import get_db
from app.models import Users, Planets

router = APIRouter(
    prefix="",
    tags=["general"],
)


@router.get("/planets", summary="Get all planets")
async def get_planets(db: Session = Depends(get_db)):
    """
    Retrieve all planets from the database
    """
    planets = db.query(Planets).all()
    return planets


@router.get("/protected", summary="Protected route example")
async def protected_route(current_user: Users = Depends(get_current_user)):
    """
    Example of a protected route that requires authentication
    """
    return {
        "message": f"Hello, {current_user.email}! This is a protected route.",
        "user_id": current_user.id,
    }


@router.get("/{item_id}", summary="Get an item by ID")
def read_item(item_id: int, q: Optional[str] = None):
    """
    Get details of a specific item
    """
    return {"item_id": item_id, "q": q}
