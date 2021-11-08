def countArithmeticMean(a):
    count = 0
    for i in range(len(a)):
        if i == 0:
            prev_no = 0
        else:
            prev_no = a[i-1]

        if i == len(a) - 1:
            next_no = 0
        else:
            next_no = a[i+1]

        if prev_no + next_no == a[i] * 2:
            count += 1

    return count

print(countArithmeticMean([2, 4, 6, 6, 3]))
