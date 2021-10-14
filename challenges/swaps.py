def areAlmostEqual(input_list):
    test = input_list[:]
    test.sort()
    ind = []

    for i in range(len(input_list)):
        if input_list[i] != test[i]:
            ind.append(i)
        if len(ind) > 2:
            return False

    return (input_list[ind[0]] == test[ind[-1]]) and (input_list[ind[-1]] == test[ind[0]])

print(areAlmostEqual([1000, 10, 100]))