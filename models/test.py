import json
from __init__ import User


if __name__ == "__main__":

    with open("data/user.json") as f:
        data = json.load(f)

    user = User.model_validate(data)

    print(user)


    #-------------------------------------------------


    with open("data/users.json") as f:
        data = json.load(f)

    users = [User.model_validate(user) for user in data]

    print(users)
