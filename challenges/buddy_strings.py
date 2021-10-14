"""Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad"."""
def buddyStrings(s, goal):
    a = s
    b = goal

    l = len(a)
    l3 = len(b)
    if l != l3:
        return False
    c = 0
    l1 = []
    l2 = []
    # Check the different characters and put them in l1 and l2
    for i in range(l):
        if a[i] != b[i]:
            c = c + 1
            l1.append(a[i])
            l2.append(b[i])

    # Check if there are more than 2 different characters or if there's just 1 and return False
    if c > 2 or c == 1:
        return False

    elif c == 2:
        # Check if swapping them will make an equal value
        if l1[0] == l2[1] and l1[1] == l2[0]:
            return True
        else:
            return False
    else:
        # Swap them all and check if one of the swaps will work
        for i in range(l - 1):
            for j in range(i + 1, l):
                if a[i] == b[j] and a[j] == b[i]:
                    return True
        return False

print(buddyStrings("abab", "abab"))