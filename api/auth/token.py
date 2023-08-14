from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from api.auth.exceptions import USER_UNAUTHORIZED, LOGIN_EXPIRED
# to get a string like this run:
# openssl rand -hex 32
# TODO: get secret key from env file
SECRET_KEY = "4986b74f93f0eb4df5fc42bbc03d741d11a169f55392a1995e69994c5cf5976b"
ALGORITHM = "HS256"
TOKEN_EXPIRES_M = 60


class Token(BaseModel):
    access_token: str
    token_type: str


def create(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRES_M)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise LOGIN_EXPIRED
    except JWTError:
        raise USER_UNAUTHORIZED
