# imports the Block class from block.py
from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = {}
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)
        return self.chain

    # prints contents of blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

            # add block to blockchain `chain`

    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain) - 1].hash
        new_block = Block(transactions, previous_block_hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            # If the current hash isn't correct the blockchain is invalid
            if not current.hash == current.generate_hash():
                return False

            # If the previous hash isn't correct the blockchain is invalid
            if not current.previous_hash == previous.generate_hash():
                return False
        return True
