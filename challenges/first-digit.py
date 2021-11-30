# Find the leftmost digit that occurs in a given string.
def solution(inputString):
    for i in inputString:
        if i.isdigit():
            return i

print(solution("var_1__Int"))