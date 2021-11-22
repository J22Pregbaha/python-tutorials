# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two
# neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).
#
# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.
def solution(n, firstNumber):
    halfway_mark = n / 2
    if firstNumber >= halfway_mark:
        return firstNumber - halfway_mark
    else:
        return firstNumber + halfway_mark

# OR
def solution2(n, firstNumber):
    return (firstNumber + n / 2) % n

print(solution2(10, 2))