def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    for i in range(len(s)):
        j = 2
        while j <= len(s):
            if s[0:i] * j == s:
                return True
            j += 1
    return False

def repeatedSubstringPatternTwo(s):
    """
    :type s: str
    :rtype: bool
    """
    for i in range(1, len(s)):
        test_str = s
        new = test_str.replace(s[0:i], "")
        if len(new) == 0:
            return True
    return False

def repeatedSubstringPatternThree(s):
    """
    :type s: str
    :rtype: bool
    """
    print(s[1:], s[:-1])
    return s in s[1:] + s[:-1]


print(repeatedSubstringPattern("abcabcabcabc")) # Too slow
print(repeatedSubstringPatternTwo("aa")) # Only faster than 5.17% of the submissions
print(repeatedSubstringPatternThree("abcabcabcab")) # From the discussions

