# You are given an array of integers a and two integers l and r.
# Your task is to calculate a boolean array b, where b[i] = true if there exists an integer x,
# such that a[i] = (i + 1) * x and l ≤ x ≤ r. Otherwise, b[i] should be set to false.
def boundedRatio(a, l, r):
    final_array = []

    for index, element in enumerate(a):
        count = 0
        for i in range(l, r + 1):
            if (index + 1) * i == element:
                count += 1
                break
        if count > 0:
            final_array.append(True)
        else:
            final_array.append(False)

    return final_array

