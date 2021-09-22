def isValid(s):
    opening = "{[("
    closing = "}])"
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            # Return false if there's no opening bracket
            if len(stack) == 0:
                return False

            # Remove the opening bracket if that's the last thing in the stack. If it's another opening bracket, return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(isValid("[([]])"))