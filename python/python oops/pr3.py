class Bank_account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def credit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("total amount",self.balance)
        else:
            return False
        
    def deposite(self,amount):
        if self.balance > amount :
            self.balance = self.balance - amount 
            print("remaing amount",self.balance)
        else:
            return False 
        
    @staticmethod
    def is_valid_amount(amount):
        if amount > 0 :
            return True
        else:
            return False
        
s1 = Bank_account("BA",10000)
s1.credit(200)
s1.deposite(100)
s1.is_valid_amount(500)
