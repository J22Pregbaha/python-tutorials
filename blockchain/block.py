from datetime import datetime
from hashlib import sha256


class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def print_block(self):
        # prints block contents
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())

    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.transactions) + str(self.nonce) + str(self.previous_hash)

        # hash the blocks contents
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)