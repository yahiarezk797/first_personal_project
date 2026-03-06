class Accounts:
    def __init__(self, id, name,pwd, money):
        self.id = id
        self.name = name
        self.pwd = pwd
        self.money = money

    def __eq__(self, acc):
        return (self.pwd == acc.pwd and self.id == acc.id and self.name == acc.name)
    
    def trans(self, acc, amount):
        if amount <= 0:
            raise ValueError("Das Betrag soll positiv sein.")
        if self.money < amount:
            return False
        self.money -= amount
        acc.money += amount
        return True

    def add(self, amount):
        if amount <= 0:
            raise ValueError("Das Betrag soll positiv sein.")
        self.money += amount

