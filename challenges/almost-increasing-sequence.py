def almostIncreasingSequence(sequence):
    new_sequence = sequence[:]
    for i in range(len(sequence)):
        new_sequence.pop(i) # Remove the element

        if new_sequence == sorted(set(new_sequence)): # Check if it's equal to the sorted list without duplicates
            return True

        new_sequence = sequence[:]
    return False

# OR
def almostIncreasingSequence2(sequence):
    problemHere = problemAhead = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            problemHere += 1
        if i + 2 < len(sequence) and sequence[i] >= sequence[i + 2]:
            problemAhead += 1
    return problemHere < 2 and problemAhead < 2

print(almostIncreasingSequence2([1, 3, 2]))