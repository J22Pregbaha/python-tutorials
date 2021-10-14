def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0

    if haystack.find(needle) != -1:
        return haystack.find(needle)
    else:
        return -1

print(strStr("aaaaa", "bba"))