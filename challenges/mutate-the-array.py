def mutateTheArray(n, a):
    newArray = []
    for i in range(len(a)):
        if i - 1 < 0:
            first = 0
        else:
            first = a[i - 1]

        if i + 1 == n:
            last = 0
        else:
            last = a[i + 1]

        print(first, a[i], last)

        newValue = first + a[i] + last
        newArray.append(newValue)
    return newArray

print(mutateTheArray(5, [4, 0, 1, -2, 3]))
