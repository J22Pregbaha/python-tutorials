# Given a string s, determine if it is valid.
#
# A string s is valid if, starting with an empty string t = "",
# you can transform t into s after performing the following operation any number of times:
#
# Insert string "abc" into any position in t.
# More formally, t becomes tleft + "abc" + tright, where t == tleft + tright.
# Note that tleft and tright may be empty.
# Return true if s is a valid string, otherwise, return false.
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for i in s:
        if i == "a":
            stack.append(i)
        if i == "b":
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == "a":
                    stack.append(i)
                else:
                    return False
        if i == "c":
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == "b":
                    stack.pop()
                    stack.pop()
                else:
                    return False
    return len(stack) == 0

print(isValid("abc"))