"""You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false."""

def areAlmostEqual(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if s1 == s2:
        return True

    ind = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ind.append(i)
    
    if len(ind) > 2:
        return False

    return (s1[ind[0]] == s2[ind[-1]]) and (s1[ind[-1]] == s2[ind[0]])

print(areAlmostEqual("bank", "bnak"))