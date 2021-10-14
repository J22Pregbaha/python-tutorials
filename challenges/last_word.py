def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    str_lst = s.split()
    last_word = str_lst[-1]
    return len(last_word)

print(lengthOfLastWord("   fly me   to   the moon  "))