# Write a function that reverses characters in (possibly nested) parentheses in the input string.
# Input strings will always be well-formed with matching ()s.
def reverseInParentheses(s):
    evaluation = '"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"'
    print(evaluation)
    return eval(evaluation)

print(reverseInParentheses("(bar)baz(blim)"))