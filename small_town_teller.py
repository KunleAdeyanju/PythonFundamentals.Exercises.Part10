
class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id                    # has to be unique
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name} is a person with id {self.id}"

class Account:
    
    def __init__(self, number, type, owner, balance):
        self.number = number            # has to be unique
        self.type = type
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner.first_name} is the owner of \naccount number: {self.number}\nType: {self.type}\nBalance: {self.balance}"

class Bank:
    def __init__(self):
        self.customer: dict[int, Person] = dict()
        self.account: dict[int, Account] = dict()
        

    def new_customer(self, customer: Person) -> None:
        if customer.id in self.customer:
            raise ValueError(f"This id {customer.id} already exists in the sytem")
        else:
            self.customer[customer.id] = customer


    def new_account(self, account: Account) -> None:
        if account.owner.id not in self.customer:
            raise ValueError(f"{account.owner.id} doesn't exist in the the system")
        elif account.number in self.account:
            raise ValueError(f"{account.number} is already being used by another account")
        else:
            self.account[account.number] = account

    def remove_account(self, account: Account) -> None:
        if account.number not in self.account:
            raise ValueError(f"{account.number} doesn't exist in the the system")
        else:
            self.account = {y: x for y, x in self.account.items() if x != account}

    def deposit(self, account_num: int, depo: float):
        if account_num in self.account:
            account = self.account.get(account_num)
            account.balance = round (account.balance + depo, 2)
        else:
            raise ValueError(f"Haveing trouble finding this account")
 

    def withdrawal(self, account_num: int, withd: float):
        if account_num in self.account:
            account = self.account.get(account_num)
            account.balance = round (account.balance - withd, 2)
        else:
            raise ValueError(f"Haveing trouble finding this account")

    def balance_inquiry(self, account_num:int)->float:
        if account_num in self.account:
            account = self.account.get(account_num)
            return account.balance
        else:
            raise ValueError(f"Haveing trouble finding this account")