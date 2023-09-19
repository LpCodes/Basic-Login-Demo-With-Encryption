import json
from pathlib import Path
import sys
import cryptocode

DATA_FILE = "cd.json"
ENCRYPTION_KEY = "123"

def check_or_create_data_file():
    """Check if the data file exists; if not, create it."""
    cur_dir = Path.cwd()
    file = cur_dir / DATA_FILE

    if file.exists():
        print("OLD Json Data file already exists")
        return load_data_from_file(file)
    else:
        print("Creating a new JSON data file as old data was not present")
        return {}

def load_data_from_file(file):
    """Load data from the given JSON file."""
    with open(file, "r") as json_file:
        return json.load(json_file)

def save_data_to_file(data, file):
    """Save data to the given JSON file."""
    with open(file, "w") as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)

def register_user(data):
    """Register a new user."""
    while True:
        uname = input("Enter username:\n")
        if uname in data:
            print("Username already exists. Please choose a different one.")
        else:
            break

    pwd = input("Enter password:\n")
    encrypted_pwd = encrypt_password(pwd)
    return uname, encrypted_pwd

def encrypt_password(password):
    """Encrypt the given password."""
    return cryptocode.encrypt(password, ENCRYPTION_KEY)

def verify_login(data):
    """Verify user login."""
    print("#" * 50 + "Login" + "#" * 50)
    uname = input("Please Enter login Username:\n")
    pwd = input("Please Enter Login Password:\n")

    try:
        encrypted_pwd = data[uname]
        if cryptocode.decrypt(encrypted_pwd, ENCRYPTION_KEY) == pwd:
            print("Login successful")
        else:
            print("Login failed")
    except KeyError:
        print("Username does not exist")
        user_response = input("Do you want to create a new user? (Y/N):\n")
        if user_response.capitalize() == "Y":
            username, password = register_user(data)
            encrypted_password = encrypt_password(password)
            data[username] = encrypted_password
            save_data_to_file(data, DATA_FILE)
            print("User added successfully. Please rerun the login to try again.")
        else:
            sys.exit()

if __name__ == "__main__":
    data = check_or_create_data_file()
    print("Current JSON data:\n", data)
    verify_login(data)
