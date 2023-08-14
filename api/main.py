import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import api.auth.token as token
import api.database.wrapper as database
from api.auth.exceptions import USER_UNAUTHORIZED, USER_EXISTS
from api.auth.user import authenticate_user, get_user_from_db, UserRegistration
from api.auth.passwd import generate_hashed_pwd

load_dotenv()

app = FastAPI()

users_dict = database.get_users()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token_: str = Depends(oauth2_scheme)):
    try:
        payload = token.decode(token_)
        username: str = payload.get("sub")
        if username is None:
            raise USER_UNAUTHORIZED
    except Exception as e:
        raise e
    user = get_user_from_db(username=username, db=users_dict)
    if user is None:
        raise USER_UNAUTHORIZED
    return user


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login", response_model=token.Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password, users_dict)
    if not user:
        raise USER_UNAUTHORIZED
    access_token = token.create(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/register")
def register_user(form_data: UserRegistration = Depends()):
    print(form_data)
    username = form_data.username
    if username in users_dict:
        raise USER_EXISTS

    full_name = form_data.full_name
    email = form_data.email
    hashed_password = generate_hashed_pwd(form_data.password)
    database.insert_user(
        {
            "username": username,
            "full_name": full_name,
            "email": email,
            "hashed_password": hashed_password,
        }
    )
    return {"status": "ok"}


@app.post("/chat")
async def chat(token_: str = Depends(get_current_user)):
    # return random
    from random import randint
    random_nr = randint(0, 100)
    return {"status": "ok", "message": f"Hello World {random_nr}"}
