
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from fastapi_socketio import SocketManager

import api.auth.token as token
import api.database.wrapper as database
from api.auth.exceptions import HTTP_USER_UNAUTHORIZED, HTTP_USER_EXISTS, UserUnauthorized, LoginExpired
from api.auth.user import authenticate_user, get_user_from_db, UserRegistration
from api.auth.passwd import generate_hashed_pwd
from chatbot.orchestrator import Orchestrator

load_dotenv()

app = FastAPI()
sio = SocketManager(app=app)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
orchestrators_dict = {}
sid_username_dict = {}


async def get_current_user(token_: str = Depends(oauth2_scheme)):
    try:
        payload = token.decode(token_)
        username: str = payload.get("sub")
        if username is None:
            raise HTTP_USER_UNAUTHORIZED
    except Exception as e:
        raise e
    user = get_user_from_db(username=username, db=database.get_users())
    if user is None:
        raise HTTP_USER_UNAUTHORIZED
    return user


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login", response_model=token.Token)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(
        form_data.username, form_data.password, database.get_users()
    )
    if not user:
        raise HTTP_USER_UNAUTHORIZED
    access_token = token.create(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/register")
def register_user(form_data: UserRegistration = Depends()):
    print(form_data)
    username = form_data.username
    if username in database.get_users():
        raise HTTP_USER_EXISTS

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
    from random import randint
    random_nr = randint(0, 100)
    return {"status": "ok", "message": f"Hello World {random_nr}"}


@sio.on('connect')
async def handle_connect(sid, environ):
    # get token from query parameter
    from urllib.parse import parse_qs
    token = parse_qs(environ['QUERY_STRING']).get('token')[0]
    print(f"Token: {token}")
    try:
        await get_current_user(token)
    except UserUnauthorized as e:
        print(f"Unauthorized. Will not connect")
        await sio.emit('chat-rsp', {'status': 'error', 'message': 'Unauthorized'})
        return False
    except LoginExpired as e:
        print(f"Login expired. Will not connect")
        await sio.emit('chat-rsp', {'status': 'error', 'message': 'Login expired'})
        return False

    global orchestrators_dict
    user = await get_current_user(token)
    orchestrators_dict[user.username] = Orchestrator(user.username)
    sid_username_dict[sid] = user.username
    bot_reply, _ = orchestrators_dict[user.username].reply(None)
    print(f"AI: {bot_reply}")
    await sio.emit('chat-rsp', bot_reply)


@sio.on('disconnect')
async def handle_disconnect(sid):
    print(f"Disconnected {sid}")


@app.sio.on('chat')
async def chat(sid, *args, **kwargs):
    input = args[0]
    print(f"Received {input} from {sid}")
    username = sid_username_dict[sid]
    bot_reply, _ = orchestrators_dict[username].reply(input)
    await sio.emit('chat-rsp', f"{bot_reply}")
