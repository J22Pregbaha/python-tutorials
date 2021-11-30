# Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.
#
# Given an integer, find its digit degree.
#
# Example
#
# For n = 5, the output should be
# solution(n) = 0;
# For n = 100, the output should be
# solution(n) = 1.
# 1 + 0 + 0 = 1.
# For n = 91, the output should be
# solution(n) = 2.
# 9 + 1 = 10 -> 1 + 0 = 1.
def solution(n):
    count = 0
    while True:
        a = list(str(n))
        if len(a) == 1:
            return count
        n = sum(map(int, a))
        count += 1

# OR
def solution2(n):
    d=0
    while n>=10:
        n=sum([int(i) for i in str(n)])
        d+=1
    return d

print(solution(5))