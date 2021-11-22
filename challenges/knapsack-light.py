# You found two items in a treasure chest!
# The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2.
# What is the total maximum value of the items you can take with you, assuming that your max weight capacity is
# maxW and you can't come back for the items later?
#
# Note that there are only two items and you can't bring more than one item of each type,
# i.e. you can't take two first items or two second items.
def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2

    stack = [0]
    if weight1 <= maxW:
        stack.append(value1)
    if weight2 <= maxW:
        if value2 > stack[-1]:
            stack.append(value2)

    return stack[-1]

# OR
def solution2(value1, weight1, value2, weight2, maxW):
    return max(value1 + value2 if weight1 + weight2 <= maxW else 0, value1 if weight1 <= maxW else 0, value2 if weight2 <= maxW else 0)

print(solution2(15, 2, 20, 3, 2))
