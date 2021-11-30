# You have deposited a specific amount of money into your bank account.
# Each year your balance increases at the same growth rate.
# With the assumption that you don't make any additional deposits,
# find out how long it would take for your balance to pass a specific threshold.
def solution(deposit, rate, threshold):
    i = 0
    while deposit < threshold:
        deposit += (rate/100) * deposit
        i += 1
    return i

print(solution(100, 20, 170))