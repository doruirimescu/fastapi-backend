# Starting template for a fastapi backend

## How to run
### Install from source
1. clone this repo and cd into it
2. populate .env with your credentials
3. create environment variables `cp example-env.env .env`
4. create a python venv `python3.10 -m venv venv`
5. activate the virtual environment `source venv/bin/activate`
6. install requirements `pip install -r requirements.txt`

#### Run backend
1. run `uvicorn api.main:app --reload`
2. navigate to http://127.0.0.1:8000/docs

#### Run websocket frontend mock
1. open [socket_example.html](https://github.com/doruirimescu/fastapi-backend/blob/master/socket_example.html) with browser
2. login user via /login endpoint, get the token
3. replace the token in [html](https://github.com/doruirimescu/fastapi-backend/blob/9fea52b69011cf40c197d3e63ad6889c4c5f08c0/socket_example.html#L9)

## TODO
Dockerize
Unit tests
