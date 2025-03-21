from small_town_teller import Person, Account
from persistent_small_town_teller import Bank2


# zc_bank = Bank2()
# bob = Person(1, "Bob", "Smith")

# # print(bob)

# zc_bank.new_customer(bob)
# bob_savings = Account(101, "Savings", bob, 0.00)

# # print(bob_savings)

# zc_bank.new_account(bob_savings)

# #print(zc_bank.account)
# #print(zc_bank.balance_inquiry(101))

# print(zc_bank. customer)
# print(zc_bank.account)

# zc_bank.save_data()

zc_bank = Bank2()
print(zc_bank. customer)
print(zc_bank.account)

zc_bank.load_data()
print(zc_bank. customer)
print(zc_bank.account)