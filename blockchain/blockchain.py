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
        # Calculate proof for new block
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)

        # Return, in order, the calculated proof and the new_block itself
        return proof, new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            # If the current hash isn't correct the blockchain is invalid
            if current.hash != current.generate_hash():
                print("The current hash of the block does not equal the generated hash of the block.")
                return False

            # If the previous hash isn't correct the blockchain is invalid
            if current.previous_hash != previous.generate_hash():
                print("The previous block's hash does not equal the previous hash value stored in the current block.")
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        not_yet = True
        while not_yet:
            proof = block.generate_hash()
            # Check if the first two (because the current difficulty is 2) characters are numbers and check if they are 0
            # If they are then return False to show that we've found the correct proof
            if proof[0:difficulty].isnumeric():
                if int(proof[0:difficulty]) == 0:
                    not_yet = False

            block.nonce = block.nonce + 1
        block.nonce = 0
        return proof
