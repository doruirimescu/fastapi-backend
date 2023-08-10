from typing import Optional
from fastapi import FastAPI, HTTPException, status, Form, Header
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from dotenv import load_dotenv
import os
from api.auth.user import UserInDb, authenticate_user
import api.auth.token as token
import api.database.wrapper as database

load_dotenv()

print(os.getenv("TEST"))

app = FastAPI()

# should load from db json
users_dict = database.get_users()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    for i in range(item_id):
        print(i)
    return {"item_id": item_id, "q": q}


@app.get("/large-task-sync")
def time_consuming_task(n: int):
    import time
    print("Sleeping for", n, "seconds")
    time.sleep(n)
    print("done")
    return {"n": n}


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
