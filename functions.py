import os
from pathlib import *
import csv
from accounts import *
from datetime import datetime
from main import ph

def id_gen():
    return len(os.listdir("./accounts")) - 1
    
def creat_an_account(name, pwd, amount):
    id = id_gen()
    acc = Accounts(id, name, pwd, amount)
    data = {"id": acc.id, "name": acc.name, "password": acc.pwd, "money": acc.money}
    try:
        os.mkdir(os.path.join(f"./accounts/{id}"))
        with open(f"./accounts/{id}/info.csv", "w") as f:
            fields = data.keys()
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerow(data)
        with open("./accounts/accounts.csv", "a") as file:
            fields = data.keys()
            writer = csv.DictWriter(file, fieldnames=fields)
            if id == 0:
                writer.writeheader()
            writer.writerow(data)
        return f"The account has been created\nID:{id}"
    except Exception as e:
        return e
    
def log_in(id, name, pwd):
    try:
        if not os.path.exists(f"./accounts/{id}"):
            raise Exception("There is no account with this ID!")
        with open(f"./accounts/{id}/info.csv", "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)[0]
        if name != data["name"]:
            raise Exception("Wrong Name!")
        if not ph.verify(data["password"], pwd):
            raise Exception("Wrong Password!")
        account = Accounts(data["id"], data["name"], data["password"], data["money"])
        return account
    except Exception as e:
        return e
    
def history_update(acc, row):
    with open(f"./accounts/{acc.id}/history.csv", "a") as f3:
            writer2 = csv.writer(f3)
            writer2.writerow(row)

def accounts_update(acc):
    dict_acc = acc.to_dict()
    with open(f"./accounts/{acc.id}/info.csv", "w") as f:
        fields = dict_acc.keys()
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerow(dict_acc)
                           
    with open("./accounts/accounts.csv", "r") as f1:
        reader = csv.DictReader(f1)
        rows = list(reader)
        rows[acc.id]["money"] = acc.money
            
    with open("./accounts/accounts.csv", "w") as f2:
        fields = dict_acc.keys()
        writer = csv.DictWriter(f2, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def pull_money(acc, amount):
    try:
        if amount > acc.money:
            print("Your money is not enough")
            return
        acc.pull(amount)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        his = ["Pulling money", time, amount]
        accounts_update(acc)
        history_update(acc, his)
        print("Succeeded!")
    except Exception as e:
        print(e)

def put_money(acc, amount):
    try:
        acc.add(amount)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = ["Add money", time, amount]
        history_update(acc, row)
        accounts_update(acc)
        print("Succeeded!")
    except Exception as e:
        print(e)

def transfer_money(acc1, acc2, amount):
    try:
        if amount > acc1.money:
            print("Your money is not enough")
            return
        acc1.trans(acc2, amount)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [f"Transfer money from {acc1.id} to {acc2.id}", time, amount]
        history_update(acc1, row)
        history_update(acc2, row)
        accounts_update(acc1)
        accounts_update(acc2)
        print("Succeeded!")
    except Exception as e:
        print(e)

def see_history(acc):
    with open(f"./accounts/{acc.id}/history.csv", "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        for row in rows:
            print(row)

def id_to_account(id):
    try:
        if not os.path.exists(f"./accounts/{id}"):
            raise Exception("There is no account with this id.")
        with open(f"./accounts/{id}/info.csv", "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)[0]
        account = Accounts(data["id"], data["name"], data["password"], data["money"])
    except Exception as e:
        print(e)
    return account