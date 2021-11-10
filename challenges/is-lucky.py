# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
def isLucky(n):
    n = str(n)
    halfway_point = int(len(n) / 2)

    first_half = n[:halfway_point]
    second_half = n[halfway_point:]

    first_half_sum = 0
    second_half_sum = 0

    for i in first_half:
        first_half_sum += int(i)

    for i in second_half:
        second_half_sum += int(i)

    if first_half_sum == second_half_sum:
        return True
    return False

print(isLucky(239017))