import json

with open("user-info.json", "r") as user_f:
    # Loading the ids
    user_info = json.load(user_f)

print(user_info)