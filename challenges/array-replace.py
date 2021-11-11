# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if i == elemToReplace else i for i in inputArray]

print(arrayReplace([1, 2, 1], 1, 3))