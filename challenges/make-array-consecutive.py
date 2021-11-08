def makeArrayConsecutive2(statues):
    statues.sort()
    minimum = 0

    for i in range(len(statues)):
        if i < len(statues) - 1:
            # Check where the next number is higher than it should be and check how many numbers are missing
            if statues[i+1] > (statues[i] + 1):
                minimum += statues[i+1] - statues[i] - 1

    return minimum

print(makeArrayConsecutive2([6, 2, 3, 8]))