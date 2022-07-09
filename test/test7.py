import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as file:
            username = json.load(file)
    except:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username


def  greet():
    username = get_stored_username()
    if username:
        print("Welcom back,"+username+"!")
    else:
        username = get_new_username()
        print("we'll remember you when you come back, " + username + "!")


greet()