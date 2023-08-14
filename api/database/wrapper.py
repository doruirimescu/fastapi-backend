import json


def get_users():
    with open("api/database/data/users.json") as f:
        users_dict = json.load(f)
    return users_dict


def insert_user(user: dict):
    users_dict = get_users()
    users_dict[user["username"]] = user
    with open("api/database/data/users.json", "w") as f:
        json.dump(users_dict, f, indent=4)
