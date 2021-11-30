import re
# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
#
# Check if the given string is a correct variable name.
#
# Example
#
# For name = "var_1__Int", the output should be
# solution(name) = true;
# For name = "qq-q", the output should be
# solution(name) = false;
# For name = "2w2", the output should be
# solution(name) = false.
def solution(name):
    return name.isidentifier()

# OR
def solution2(name):
    if re.match('[a-z_][0-9_a-z]*$', name, re.IGNORECASE):
        return True
    return False

print(solution2("var_1__Int"))