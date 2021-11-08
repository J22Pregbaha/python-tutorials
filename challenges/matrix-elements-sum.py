def matrixElementsSum(matrix):
    sum = 0
    for i in zip(*matrix):
        chee = list(i)
        for j in chee:
            if j == 0:
                break
            sum += j
    return sum

print(matrixElementsSum([[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]))