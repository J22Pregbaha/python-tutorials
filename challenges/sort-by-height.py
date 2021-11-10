def sortByHeight(a):
    final_array = []

    # First, deal with the non-trees. Add all of them
    for i in a:
        if i != -1:
            final_array.append(i)

    # Second, sort the non-trees in order
    final_array.sort()

    # Third, deal with the trees. Insert them in their original position
    for i in range(len(a)):
        if a[i] == -1:
            final_array.insert(i, a[i])

    return final_array

print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))