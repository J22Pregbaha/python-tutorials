def reverseBits(n):
    return int('{0:032b}'.format(n)[::-1], 2)