from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from database.models import Room
from database.schema import RoomResponseSchema
from database.database import get_db
from typing import List

router = APIRouter()

@router.get("/rooms", response_model=List[RoomResponseSchema])
def retrive_rooms(request: Request, db: Session=Depends(get_db)):
    return db.query(Room).all()