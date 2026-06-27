from pwdlib import PasswordHash
from database.models import User
from datetime import datetime, timedelta
from jose import jwt, JWTError

password_hash = PasswordHash.recommended()
SECRET_KEY = "87sadf230bjwe27240iud23973ne3ui23fg486hdf23h389ye39gd902jv52d6dm289"
ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str):
    return password_hash.verify(password, hashed_password)


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter_by(username=username).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    
    return user


def create_access_token(username: str, user_id: int, exp_delta: timedelta):
    encode = {"sub": username, "id": user_id, "exp": datetime.now() + exp_delta}
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)