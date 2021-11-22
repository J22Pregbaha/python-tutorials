# Consider an arithmetic expression of the form a#b=c.
# Check whether it is possible to replace # with one of the four signs: +, -, * or / to obtain a correct expression.
def solution(a, b, c):
    return a + b == c or a - b == c or a * b == c or a / b == c

# OR
def solution2(a, b, c):
    return c in (a+b, a-b, a*b, a/b)

# OR
def solution3(a, b, c):
    return any([
        a + b == c,
        a - b == c,
        a * b == c,
        a / b == c
    ])

print(solution(2, 3, 5))