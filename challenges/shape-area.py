# Figure out the formula and use it
def shapeArea(n):
    number = 0
    output = 1
    while number < n:
        output += (4 * number)
        # print(number, output)
        number += 1
    return output

print(shapeArea(1))