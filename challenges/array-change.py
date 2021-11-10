# You are given an array of integers.
# On each move you are allowed to increase exactly one of its element by one.
# Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
def arrayChange(inputArray):
    stack = [inputArray[0]]
    moves = 0

    for i in range(1, len(inputArray)):
        # First check if this number is less than or equal to its predecessor.
        # If it isn't just add it to the stack
        # If it is, check how many numbers you need to add to make it one more than its predecessor,
        # then add the difference to the moves and add the (predecessor + 1) to the stack.
        if inputArray[i] <= stack[-1]:
            moves += (stack[-1] + 1) - inputArray[i]
            stack.append(stack[-1] + 1)
        else:
            stack.append(inputArray[i])

    return moves

print(arrayChange([-1000, 0, -2, 0]))