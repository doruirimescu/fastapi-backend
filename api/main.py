import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import api.auth.token as token
import api.database.wrapper as database
from api.auth.user import authenticate_user, get_user_from_db

load_dotenv()

print(os.getenv("TEST"))

app = FastAPI()

# should load from db json
users_dict = database.get_users()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token_: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = token.decode(token_)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except Exception as e:
        raise e
    user = get_user_from_db(username=username, db=users_dict)
    if user is None:
        raise credentials_exception
    return user


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    for i in range(item_id):
        print(i)
    return {"item_id": item_id, "q": q}


@app.post("/login", response_model=token.Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password, users_dict)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = token.create(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    for i in range(item_id):
        print(i)
    return {"item_id": item_id, "q": q}


@app.post("/chat")
async def chat(token: str = Depends(get_current_user)):
    return {"status": "ok", "message": "Hello World"}
