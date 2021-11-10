# Given two strings, find the number of common characters between them.
def commonCharacterCount(s1, s2):
    total = 0
    # Find every unique character in the first string
    for i in set(s1):
        # Count each of them in both string 1 and 2
        string1 = s1.count(i)
        string2 = s2.count(i)

        # Find the minimum number of times the unique characters in string 1 appear in string 2
        min_no = min(string1, string2)

        #Add it to the total
        total += min_no
    return total

print(commonCharacterCount("aabcc", "adcaa"))