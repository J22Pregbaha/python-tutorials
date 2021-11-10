# Given a string, find out if its characters can be rearranged to form a palindrome.
def palindromeRearranging(inputString):
    # count the number of each individual character
    # can form a palindrome only if:
    #   at most one of the character counts is odd, all others must be even

    string_array = list(inputString)
    chars = set(string_array)
    count = [string_array.count(i) % 2 for i in chars]
    return sum(count) <= 1

print(palindromeRearranging("zyyzdfdzzzz"))