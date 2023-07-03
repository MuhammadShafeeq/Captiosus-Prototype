import os
import json

class Functions:
    def __init__(self):
        return_message = """A class of user-defined functions that can be used to reduce the workload on the programmer"""
        return return_message
    def register(username, password, name):
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            print("Account already exists. ")
            return
        else:
            users[username] = {}
            users[username]["Name"] = name
            users[username]["Password"] = password
            users[username]["tdList"] = {}
            with open('data.json', 'w') as f:
                json.dump(users, f)
            print("\nPROCESS COMPLETE")

    def check_username(username):
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            return False
        else:
            return True

    def check_creds_for_login(username, password):
        with open('data.json', 'r') as f:
            users = json.load(f)
        if username in users:
            if users[username]["Password"] == password:
                return True
            else:
                return False
        else:
            return False

    def get_user(username):
        with open('data.json', 'r') as f:
            users = json.load(f)
        user = users[username]
        return user