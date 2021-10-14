def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a = int(a, 2)
    b = int(b, 2)
    c = a + b
    return bin(c)[2:]

print(addBinary("11", "1"))