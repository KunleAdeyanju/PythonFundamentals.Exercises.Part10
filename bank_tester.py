from small_town_teller import Person, Account, Bank

zc_bank = Bank()
bob = Person(1, "Bob", "Smith")

# print(bob)

zc_bank.new_customer(bob)
bob_savings = Account(101, "Savings", bob, 0.00)

# print(bob_savings)

zc_bank.new_account(bob_savings)

#print(zc_bank.account)
#print(zc_bank.balance_inquiry(101))

zc_bank.deposit(101, 256.02)
print(zc_bank.balance_inquiry(101))

zc_bank.withdrawal(101, 128)
print(zc_bank.balance_inquiry(101))