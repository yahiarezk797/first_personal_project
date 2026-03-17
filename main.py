from accounts import *
from functions import *
from argon2 import PasswordHasher


ph = PasswordHasher()

def main():
    print("Welcome!")
    print("1: Login")
    print("2: Open Account")
    x = int(input("? "))
    if x == 1:
        id = input("ID: ")
        name = input("Name: ")
        pwd = input("Passwort: ")
        acc = log_in(id, name, pwd)
        print(acc)
        print(f"Hallo, Frau/Herr {acc.name}\n")
        print(f"Money: {acc.money}")
        print("1: Pull money")
        print("2: Transfer money")
        print("3: Put money")
        print("4: See account's history")
        y = int(input("? "))
        if y == 1:
            amount = int(input("Amount: "))
            pull_money(acc, amount)
        elif y == 2:
            amount = int(input("Amount: "))
            id2 = int(input("ID: "))
            acc2 = id_to_account(id2)
            transfer_money(acc, acc2, amount)
        elif y == 3:
            amount = int(input("Amount: "))
            put_money(acc, amount)
        elif y == 4:
            see_history(acc)

    else:
        name = input("Name: ")
        pwd = ph.hash(input("Passwort: "))
        amount = input("Amount: ") 
        print(creat_an_account(name, pwd, amount))


if __name__ == "__main__":
    main()