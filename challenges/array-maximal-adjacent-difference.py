# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
def arrayMaximalAdjacentDifference(inputArray):
    differences = []

    for index, element in enumerate(inputArray):
        if index < len(inputArray) - 1:
            next_element = inputArray[index + 1]
            difference = abs(element - next_element)
            differences.append(difference)
    return max(differences)

# OR
def arrayMaximalAdjacentDifference2(a):
    return max([abs(a[i] - a[i+1]) for i in range(len(a) - 1)])

print(arrayMaximalAdjacentDifference2([10, 11, 13]))