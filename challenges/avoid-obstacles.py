# You are given an array of integers representing coordinates of obstacles situated on a straight line.
#
# Assume that you are jumping from the point with coordinate 0 to the right.
# You are allowed only to make jumps of the same length represented by some integer.
#
# Find the minimal length of the jump enough to avoid all the obstacles.
def avoidObstacles(inputArray):
    # Sort input array in ascending order
    inputArray.sort()

    # Add all numbers between 1 and the first number to the possible jump sites list
    all_jumps = list(range(1,inputArray[0]))
    # Also add the (last number + 1) in case there's no space between the numbers in the array
    all_jumps.append(inputArray[-1] + 1)
    min_jumps = 0
    # Check if there's any space and add all those coordinates as possible jump sites
    for i in range(1, len(inputArray)):
        difference = inputArray[i] - inputArray[i-1]
        if difference > 0:
            for p in range(inputArray[i-1] + 1, inputArray[i]):
                all_jumps.append(p)

    # Sort jump sites
    all_jumps.sort()
    # Check for the lowest common number that isn't a multiple
    for j in all_jumps:
        if all(i % j != 0 for i in inputArray):
            min_jumps = j
            break

    return min_jumps

# OR
def avoidObstacles2(inputArray):
    # Check for the lowest common number that isn't a multiple
    i = 2
    while True:
        if all(j % i != 0 for j in inputArray):
            return i
        i += 1

print(avoidObstacles2([19, 32, 11, 23]))