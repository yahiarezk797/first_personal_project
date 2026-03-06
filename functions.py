import os
from pathlib import *
import csv


def id_gen():
    return len(os.listdir("./accounts"))
    
def creat_an_account(name, pwd, ammount):
    id = id_gen()
    data = {"id": id, "name": name, "password": pwd, "money": ammount}
    try:
        os.mkdir(os.path.join(f"./accounts/{id}"))
        with open(f"./accounts/{id}/info.csv", "w") as f:
            fields = data.keys()
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerow(data)
        return "The account has been created"
    except Exception as e:
        return e