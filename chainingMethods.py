class User:
    def __init__(self, name, account_number, account_balance):
        self.name = name
        self.no = account_number
        self.balance = account_balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(self.balance)
        return self
        
    def transfer_money(self, to_account, amount):
        self.make_withdrawal(amount)
        to_account.make_deposit(amount)

    

Guido = User("Guido Van Rossum", '12344556667', 10)
Daniel = User("Daniel Uhr", '145675433455', 25)
Rodrigo = User("Rodrigo Fernandez", '12324554332', 40)

# print(Guido.balance)    
Guido.make_deposit(100).make_deposit(350).make_deposit(240).display_user_balance()
Daniel.make_withdrawal(30).make_withdrawal(20).make_deposit(240).make_deposit(345).display_user_balance()
Rodrigo.make_deposit(375).make_withdrawal(25).make_withdrawal(35).make_withdrawal(75).display_user_balance()
print("User: ", Guido.name, "Balance: ", Guido.balance)
print("User: ", Daniel.name, "Balance: ", Daniel.balance)
print("User: ", Rodrigo.name, "Balance: ", Rodrigo.balance)
Daniel.transfer_money(Guido, 10)
Daniel.display_user_balance()
Guido.display_user_balance()
