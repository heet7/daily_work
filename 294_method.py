class Account():

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print("Account is created for ",self.name)

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        self.show_balance()

    def withdrod(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("withdrow amount ",amount)
            self.show_balance()

        else:
            print("your current balance is {}$ so how can you withdow {}$ of amout?".format(self.balance,amount))


    def show_balance(self):
        print("your account balance is {}".format(self.balance))

if __name__ == "__main__":
    heet = Account('Heet',0)
    heet.deposit(100)
    heet.withdrod(45)