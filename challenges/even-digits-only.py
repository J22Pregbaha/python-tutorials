# Check if all digits of the given integer are even.
def evenDigitsOnly(n):
    # Check if the modulo of each number with 2 is 0 (which means it is even)
    # Sum all numbers. If any number is odd, the sum will be greater than 0
    # If the sum is zero, all numbers are even
    return sum([int(i) % 2 for i in str(n)]) == 0

print(evenDigitsOnly(248622))