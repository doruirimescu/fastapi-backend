from pydantic import BaseModel
from fastapi import HTTPException, status
from typing import Optional
from jose import JWTError
from api.auth.passwd import is_pwd_valid


class User(BaseModel):
    """Used for responses"""

    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None


class UserRegistration(User):
    """Used for registering user"""
    password: str


class UserInDb(User):
    """Used for requests"""

    hashed_password: str


def get_user_from_db(username: str, db: dict) -> UserInDb | bool:
    return UserInDb(**db[username])


def authenticate_user(
    username: str, plain_text_password: str, db: dict
) -> UserInDb | bool:
    if username not in db:
        return False

    user = get_user_from_db(username, db)
    if not is_pwd_valid(plain_text_password, user.hashed_password):
        return False
    return user
