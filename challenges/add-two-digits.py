# You are given a two-digit integer n. Return the sum of its digits.
def solution(n):
    ten = n // 10
    unit = n % 10
    print("Ten:", ten)
    print("Unit:", unit)
    return ten + unit

# OR
def solution2(n):
    ten, unit = divmod(n, 10)
    return ten + unit

print(solution2(39))

