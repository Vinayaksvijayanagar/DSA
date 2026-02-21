class Bank:
    def __init__(self,bal,acc_no):
        self.bal = bal
        self.acc_no = acc_no
        
    def credit(self,amount):
        self.bal += amount
        print("total amount",self.bal)
        
    def debit(self,amount):
        self.bal -= amount
        print("remaing amount",self.bal)
if __name__ == "__main__"   :     
    s1 = Bank(10000,1234)
    s1.credit(200)
        