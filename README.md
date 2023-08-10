# Starting template for a fastapi backend

## How to run
### Install from source
1. create environment variables `cp example-env.env .env`
2. populate .env with your credentials
3. clone this repo and cd into it
4. create a python venv `python3.10 -m venv venv`
5. activate the virtual environment `source venv/bin/activate`
6. install requirements `pip install -r requirements.txt`

#### Run backend
1. run `uvicorn api.main:app --reload`
2. navigate to http://127.0.0.1:8000/docs


## TODO
1. Add ping endpoint
2. Add login example
3. Add json user database

Dockerize
Unit tests
