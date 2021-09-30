def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    string_val = str(x)
    rev = string_val[::-1]
    return string_val == rev

print(isPalindrome(121))