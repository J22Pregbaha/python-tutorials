# Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array.
# Return the array of these digits in ascending order.
def solution(a):
    joint = ''.join(str(n) for n in a)
    unique = sorted(list(set(joint)))
    count = 0
    stack = []

    for i in unique:
        if joint.count(i) > count:
            count = joint.count(i)
            stack.clear()
            stack.append(int(i))
        elif joint.count(i) == count:
            stack.append(int(i))

    return stack

print([25, 2, 3, 57, 38, 41])