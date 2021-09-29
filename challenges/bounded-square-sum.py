def boundedSquareSum(a, b, lower, upper):
    count = 0
    for i in a:
        for j in b:
            if lower <= i ** 2 + j ** 2 <= upper:
                count += 1

    print(count)


boundedSquareSum([3, -1, 9], [100, 5, -2], 7, 99)

