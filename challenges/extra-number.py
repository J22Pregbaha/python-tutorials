# You're given three integers, a, b and c.
# It is guaranteed that two of these integers are equal to each other.
# What is the value of the third integer?
def solution(a, b, c):
    numbers = [a, b, c]
    for i in numbers:
        if numbers.count(i) == 1:
            return i

# OR
def solution2(a, b, c):
    return a ^ b ^ c

print(solution2(4000000, 3000000, 4000000))