from block import Block

class BlockChainException(Exception):
    pass

class BlockChain:
    
    def __init__(self):
        
        genesis = Block(0, "Genesis Block")
        self.chain = [genesis]
        
    def add_block(self, data):
        
        last_block = self.get_last_block()
        block = Block(self.get_last_block().index +1, data)
        
        self.chain.append(block)
    
    def get_last_block(self):
        
        return self.chain[-1]
    
coin = BlockChain()

