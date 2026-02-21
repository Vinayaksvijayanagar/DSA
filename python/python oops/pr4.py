class Account:
    bank_name = "ABC Bank"
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def get_details(self):
        print(self.account_holder,"bank_name",self.balance)
        