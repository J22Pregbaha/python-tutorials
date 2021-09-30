"""You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced."""

def balancedString(s):
    """
    :type s: str
    :rtype: int
    """
    freq = {}
    for c in s: freq[c] = 1 + freq.get(c, 0)

    ans = len(s)
    ii = 0
    for i, c in enumerate(s):
        freq[c] -= 1
        while ii < len(s) and all(freq[x] <= len(s) // 4 for x in freq):
            ans = min(ans, i - ii + 1)
            freq[s[ii]] += 1
            ii += 1
    return ans

print(balancedString("WWEQERQWQWWRWWERQWEQ"))