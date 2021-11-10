# Given a string, find out if its characters can be rearranged to form a palindrome.
def palindromeRearranging(inputString):
    # count the number of each individual character
    # can form a palindrome only if:
    # only one character is allowed to appear an odd number of times. The others must have an even count

    string_array = list(inputString)
    chars = set(string_array)
    count = [string_array.count(i) % 2 for i in chars]
    return sum(count) <= 1

print(palindromeRearranging("zyyzdfdzzzz"))