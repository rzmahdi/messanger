from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from database.schema import UserCreateSchema, Token
from database.database import get_db
from database.models import User
from services.auth_service import hash_password, authenticate_user, create_access_token, get_current_user, create_refresh_token
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
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


@router.post("/login", response_model=Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session=Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "username or password are wrong!")

    access_token = create_access_token(user.username, user.id)
    refresh_token = create_refresh_token(user.username, user.id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        }


@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return current_user