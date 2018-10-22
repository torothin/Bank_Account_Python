class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account): #subclass of the base class Account
    """this class creates checking account instances"""  #can be called by using .__doc__

    type="checking" #class variable, all instances of this class will have this value
    def __init__(self, filepath, fee):  #__init__ are constructors
        Account.__init__(self,filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance-amount-self.fee #self.balance is an instance variable

# account=Account("BankAccount.txt")
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()

checking=Checking("BankAccount.txt", 1)
checking.transfer(90)
print(checking.balance) #.balance is considered and attribute of that class instance
checking.commit()
print(checking.__doc__)
