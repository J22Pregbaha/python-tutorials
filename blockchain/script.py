from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# Instantiate a new Blockchain object
my_blockchain = Blockchain()

# Add a block and print its contents
my_blockchain.add_block(new_transactions)
# my_blockchain.print_blocks()

# Alter a block and check if chain is still valid
setattr(my_blockchain.chain[1], 'transactions', "fake_transactions")
my_blockchain.validate_chain()