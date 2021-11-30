# You are given an array of integers a and two integers l and r.
# You task is to calculate a boolean array b, where b[i] = true if there exists an integer x,
# such that a[i] = (i + 1) * x and l ≤ x ≤ r. Otherwise, b[i] should be set to false.
def solution(a, l, r):
    return_array = []
    range_l_r = list(range(l, r + 1))

    for i in range(len(a)):
        bool_value = any((i + 1) * x == a[i] for x in range_l_r)
        return_array.append(bool_value)

    return return_array
