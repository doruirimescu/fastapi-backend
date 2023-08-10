import json

def get_users():
    with open("api/database/data/users.json") as f:
        users_dict = json.load(f)
    return users_dict
