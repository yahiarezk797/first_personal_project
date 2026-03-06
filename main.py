from accounts import *
from functions import *


def main():
    name = input("Name: ")
    pwd = input("Password: ")
    ammount = input("ammount: ")
    print(creat_an_account(name, pwd, ammount))



if __name__ == "__main__":
    main()