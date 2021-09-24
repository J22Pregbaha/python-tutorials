# imports the Block class from block.py
from block import Block


class Blockchain:
    def __init__(self, chain=[], all_transactions=[]):
        self.genesis_block()
        self.chain = chain
        self.all_transactions = all_transactions

    def genesis_block(self):
        new_block = Block([], 0)
        self.chain.append(new_block)