import json
from pathlib import Path
import sys
import cryptocode
import json


def chekifoldfileexists():
    """Checking here if old file exits if not creating"""
    cur_dir = Path.cwd()
    file = Path(f"{cur_dir}/cd.json")
    # print(file)
    if file.exists():
        print("OLD Json Data file already exits")  # load existing data
        with open("cd.json", "r") as jsonFile:
            mydic = json.load(jsonFile)
            return mydic
    else:
        # create new
        print("Creating new json data file as old data was not present")
        mydic = {}
        return mydic


def Register_User(data):
    # Get usernames and passwords
    uname = input("enter uname\n\n")
    while uname in data.keys():
        print("Username already exits plz provide a new one")
        uname = input("enter uname\n\n")
        if uname not in data.keys():
            break

    pwd = input("enter pwd\n\n")

    return uname, pwd


def Encrpyt_pwd(Password):
    """Here Encrpting password"""
    return cryptocode.encrypt(Password, "123")


def adding_data_to_dic(Olddata, Username, Encrptedpass):
    Olddata[Username] = Encrptedpass
    # print(Olddata)
    return Olddata


def addind_data_to_json(data):

    with open("cd.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4, sort_keys=True)


def verify_login():
    "verifying login here"
    print("#" * 50 + "Login" + "#" * 50)
    uname1 = input("Please Enter login Username\n\n")
    pwd2 = input("Please Enter Login Password\n\n")

    try:
        with open("cd.json", "r") as file:
            data = json.load(file)
            # print(data)

            try:
                if cryptocode.decrypt(data[uname1], "123") == pwd2:
                    print("login success")
                else:
                    print("Login fail")
            except KeyError:
                Olddata = chekifoldfileexists()
                user_responce = input(
                    "Username does not exits\n\nDo you want to create a new user\n\nPress Y to create New User or any other key to exit\n\n"
                )

                if user_responce.capitalize() == "Y":

                    Username, Password = Register_User(Olddata)

                    Encrptedpass = Encrpyt_pwd(Password)

                    updated_data = adding_data_to_dic(Olddata, Username, Encrptedpass)

                    addind_data_to_json(updated_data)
                    print("User added succussfully - Rerun Login to try again")
                else:
                    sys.exit()
    except FileNotFoundError as e:
        Olddata = chekifoldfileexists()
        user_responce = input(
            "Username does not exits\n\nDo you want to create a new user\n\nPress Y to create New User or any other key to exit\n\n"
        )

        if user_responce.capitalize() == "Y":

            Username, Password = Register_User(Olddata)

            Encrptedpass = Encrpyt_pwd(Password)

            updated_data = adding_data_to_dic(Olddata, Username, Encrptedpass)

            addind_data_to_json(updated_data)

            print("User added succussfully - Rerun Login to try again")
        else:
            sys.exit()


if __name__ == "__main__":

    Olddata = chekifoldfileexists()
    print("Current json data is as below \n\n", Olddata)

    verify_login()

    # Username, Password = Register_User(Olddata)

    # # print(Username, Password)

    # Encrptedpass = Encrpyt_pwd(Password)

    # updated_data = adding_data_to_dic(Olddata, Username, Encrptedpass)

    # addind_data_to_json(updated_data)
