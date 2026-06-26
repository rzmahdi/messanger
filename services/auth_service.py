from pwdlib import PasswordHash
from database.models import User

password_hash = PasswordHash.recommended()

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