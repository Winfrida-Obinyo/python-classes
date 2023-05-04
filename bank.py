class Account:

     category = "Finance"
 
     

     def __init__(self, account_number, account_type, balance):   
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
         
     def print_details(self):
        return f"Account Number{self.account_number}, Account Type{self.account_type}, Balance{self.balance}"
    


    
        