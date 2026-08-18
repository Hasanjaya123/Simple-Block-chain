from block import Block
from block import Person

class BlockChainException(Exception):
    pass

class BlockChain:
    
    def __init__(self):
        
        genesis = Block(0, "Genesis Block")
        self.chain = []
        self.chain.append(genesis)
        
    def add_block(self, sender: Person, receiver: Person, amount: float):
        
        last_block = self.get_last_block()
        block = Block(last_block.index +1, sender, receiver, amount)
        
        self.chain.append(block)
    
    def get_last_block(self):
        
        return self.chain[-1]
    
    
kamal = Person("Kamal", 22)
nimal = Person("nimal", 24)
    
coin = BlockChain()

coin.add_block(kamal, nimal, 100.00)

