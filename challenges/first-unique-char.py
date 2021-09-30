import collections
def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    cnt = collections.Counter()

    for ch in s:
        cnt[ch] += 1

    for index in range(len(s)):
        if cnt[s[index]] == 1:
            return index
    return -1

print(firstUniqChar("leetcode"))