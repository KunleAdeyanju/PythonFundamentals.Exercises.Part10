
class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

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
        if account.owner not in self.account:
            # raise
            pass
        else:
            self.new_account[]

    def remove_account():
        pass

    def deposit():
        pass

    def withdrawal():
        pass

    def balance_inquiry():
        pass