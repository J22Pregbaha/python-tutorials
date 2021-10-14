def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    return num**0.5 == int(num**0.5)

print(isPerfectSquare(76))