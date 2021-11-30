# Reverse the order of the bits in a given integer.
#
# Example
#
# For a = 97, the output should be
# solution(a) = 67.
#
# 97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.
#
# For a = 8, the output should be
# solution(a) = 1.
def solution(a):
    return int(bin(a).replace('0b', '')[::-1], 2)

print(solution(97))