# Starting template for a fastapi backend

## How to run
### Install from source
1. clone this repo and cd into it
2. create a python venv `python3.10 -m venv venv`
3. activate the virtual environment `source venv/bin/activate`
4. install requirements `pip install -r requirements.txt`

#### Run backend
1. change into api `cd api`
2. uvicorn main:app --reload
3. navigate to http://127.0.0.1:8000/docs


## TODO
1. Add ping endpoint
2. Add login example
3. Add json user database 

Dockerize
Unit tests
