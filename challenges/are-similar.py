# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
# Given two arrays a and b, check whether they are similar.
def areSimilar(a, b):
    # First check if the lengths are equal
    if len(a) != len(b):
        return False

    # Than check if all elements are equal
    if sorted(a) != sorted(b):
        return False

    # Then check how many elements are out of place in the next array
    count = 0
    for index, element in enumerate(a):
        if element != b[index]:
            count += 1

    # If out of place elements are more than 2 then it'll need more than one swap
    return count <= 2

print(areSimilar([1, 1, 4], [1, 2, 3]))