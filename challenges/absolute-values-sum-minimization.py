def solution(a):
    value_stack = []
    stack = []
    for i in range(len(a)):
        value = sum([abs(x - a[i]) for x in a])
        if i == 0:
            stack.append(a[i])
            value_stack.append(value)
        else:
            if value < value_stack[-1]:
                stack.append(a[i])
                value_stack.append(value)

    return stack[-1]

print(solution([2, 4, 7]))