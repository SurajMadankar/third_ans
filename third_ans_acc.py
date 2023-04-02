class Account:

    def __init__(self,title,balance):
        self.title=title
        self.balance=balance

    def ti(self):
        print(self.title)
    def bal(self):
        print(self.balance)
    

        

class SavingsAccount(Account):

    def __init__(self,interstRate):
        self.interestRate=interstRate
    def int(self):
        print(self.interestRate)
    def all(self):
        print("Ashish",5000,self.interestRate)

obj=Account("Ashish",5000)
obj.ti()
obj.bal()
obj1=SavingsAccount(5)
obj1.int()
obj1.all()

