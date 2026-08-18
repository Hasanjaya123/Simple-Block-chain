import hashlib
import json

class MaxTransactionLimitException(Exception):
    pass
    

class Block:
    
    def ___init__(self, transaction: Transaction):
        
        self.transactions = []
        self.hash = hashlib.sha256(str(transaction).encode()).hexdigest()
        
    def validate_transations(self, transaction: Transaction):
        
        if self.transactions >= 10:
            self.transactions.append(transaction)
        
        else:
            raise MaxTransactionLimitException("Only Maximum of 10 Transactions can be added to an oneblock")
            

    def __repr__(self):
        return f"{self.sender} sent {self.reciver} Rs.{self.amount}"
    
    
class Transaction():
    
    def __init__(self, index: int, sender: Person, receiver: Person, amount: float):
        
        self.index = index
        self.sender = sender
        self.reciver = receiver
        self.amount = amount
        
    def __str__(self): 
            
        transaction = {
                    "Index" : self.index,
                    "Sender's Name": self.sender,
                    "Reciver's Name": self.reciver,
                    "Amount": f"Rs.{self.amount}"
                }
        return json.dumps(transaction, indent=4)
        
    def __repr__(self): 
        
        transaction = {
                    "Index" : self.index,
                    "Sender's Name": self.sender,
                    "Reciver's Name": self.reciver,
                    "Amount": f"Rs.{self.amount}"
                }
        return json.dumps(transaction, indent=4)
        
        
class Person:
    
    def __init__(self, name:str, age: int):
        
        self.name = name
        self.age = age
        
        