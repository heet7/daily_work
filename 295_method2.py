import pytz
import datetime

class Account(object):
    """
    Bank Account simple program

    methods:
        deposite (float) : deposite some amount
        withdrow (float) : withdrow some amount
        show_transction  : will give you full transction history
        show_balance : will display current balance
    """

    #if anythings is declare this area then it's called Attriute like
    #a = 123

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self,name,balance):
        """
        Account init method

        parameters:
            name (str) : The name of the person
            balance (float) : starting account balance                
        
        return:
            account holder name
        """
        self._name = name
        self.__balance = balance
        self._transection_list = [(Account._current_time(),self.__balance)]
        print("Account created for",self._name)

    def deposit(self,amount:float) -> float:
        """
        deposit function 
        
        parameter:
            amount : deposite amount 

        return:
            add the deposite in current balance
        """
        if amount > 0:
            self.__balance += amount
            self._transection_list.append((Account._current_time(),amount)) #Account._current_time() we use hear class name why? static method
            self.show_balance()

    def withdrow(self,amount:float) -> float:
        """
        withdrow function

        praameter:
            amount : withdrow amount

        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount            
            self._transection_list.append((Account._current_time(),-amount))
        else:
            print("you don't have enought amount in your account! Entered amount must be gerater then zero & no more then your current amount!")
        self.show_balance()

    def show_balance(self) -> float:
        """show the balance of the account"""
        print("Balance is",self.__balance)

    def show_transction(self):
        """display the transction history"""
        for time , amount in self._transection_list:
            if amount > 0:
                t_type = "Deposit "
            else:
                t_type = "Withdrow"
                self.__balance *= -1
            print("{:.5f}".format(amount)+chr(9)+"{} on {} (local time is {})".format(t_type,time,time.astimezone()))
        print("your account balance is {}".format(abs(self.__balance)))


if __name__ == "__main__":
    heet = Account("heet",100)
    heet.deposit(100)

    # heet._Account__balance = 50000 #accessing private variale

    heet.withdrow(50)
    heet.withdrow(100)
    heet.deposit(20)
    heet.show_transction()

    print()
    shyam = Account("Kumar",500)
    shyam.withdrow(100) 
    shyam.withdrow(500)
    shyam.show_transction()    

    print(Account.__doc__)

    print(help(Account))