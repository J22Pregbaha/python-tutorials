def thousandSeparator(n):
    """
    :type n: int
    :rtype: str
    """
    string = str(n)
    rev = string[::-1]
    output = ""
    n = 3
    split_string = [rev[i:i + n] for i in range(0, len(rev), n)]

    if len(string) == 3:
        return string
    for i in range(len(split_string)):
        if i != len(split_string) - 1:
            output = output + split_string[i] + "."
        else:
            output = output + split_string[i]
    return output[::-1]

print(thousandSeparator(1234))