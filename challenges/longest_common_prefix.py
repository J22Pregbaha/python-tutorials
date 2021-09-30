def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    result = ''
    for x in zip(*strs):

        # then x will be
        # ('f', 'f', 'f')
        # ('l', 'l', 'l')
        # ('o', 'o', 'i')
        # ('w', 'w', 'g')
        if len(set(x)) == 1:
            result += x[0]
        # here set(x) will be
        # {'f'}
        # {'l'}
        # {'i', 'o'}
        # {'w', 'g'}
        else:
            break
    return result

"""OR"""
def longest(strs):
    res = ""
    first_element = strs[0]
    for i in range(len(first_element)):
        for s in strs:
            if i == len(s) or s[i] != first_element[i]:
                return res
        res += first_element[i]

print(longest(["flower","flow","flight"]))