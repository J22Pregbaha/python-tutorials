def allLongestStrings(inputArray):
    count = 0
    for i in inputArray:
        if len(i) > count:
            count = len(i)

    longest_strings = []
    for i in inputArray:
        if len(i) == count:
            longest_strings.append(i)

    return longest_strings

print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))