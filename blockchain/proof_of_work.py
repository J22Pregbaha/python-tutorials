new_transactions = [{'amount': '30', 'sender': 'alice', 'receiver': 'bob'},
                    {'amount': '55', 'sender': 'bob', 'receiver': 'alice'}]

# import sha256
from hashlib import sha256

# sets the amount of leading zeros (difficulty) that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof
transaction = str(new_transactions) + str(nonce)
proof = sha256(transaction.encode()).hexdigest()

# printing proof
print(proof)

# finding a proof that has 2 leading zeros
not_yet = True
while not_yet:
    transaction = str(new_transactions) + str(nonce)
    proof = sha256(transaction.encode()).hexdigest()
    if proof[0:difficulty].isnumeric():
        if int(proof[0:difficulty]) == 0:
            final_proof = proof
            not_yet = False
    nonce = nonce + 1

# printing final proof that was found
print(final_proof)
