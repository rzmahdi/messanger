from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from database.schema import UserCreateSchema, UserResponseSchema, UserLoginSchema
from database.database import get_db
from database.models import User
from services.auth_service import hash_password, verify_password

router = APIRouter()


@router.post("/register", response_model=UserResponseSchema)
def register(request: UserCreateSchema, db: Session = Depends(get_db)):
    existing_user = (
        db.query(User)
        .filter_by(username=request.username)
        .first()
    )
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user allready exists!")
    

    new_user = User(username=request.username, password_hash=hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=UserResponseSchema)
def login(request: UserLoginSchema, db: Session=Depends(get_db)):
    existing_user = (
        db.query(User)
        .filter_by(username=request.username)
        .first()
    )

    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="username or password are wrong!")
    
    if not verify_password(existing_user.password_hash, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="username or password are wrong!")

    return existing_user