def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    string_val = str(x)
    rev = string_val[::-1]
    if rev[-1] == "-":
        new_string = rev.replace("-", "")
        rev = "-" + new_string

    # Account for constraints
    if not -2 ** 31 <= int(rev) <= 2 ** 31 - 1:
        return 0
    return int(rev)

print(reverse(1534236469))