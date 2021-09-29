from collections import Counter
def frequency_sort(s):
    # get the frequency of the most common chars
    # ex: for 'tree' -> [('e', 2), ('t', 1), ('r', 1)]
    freqs = Counter(s).most_common()
    ans = ""
    # iterate over most common chars and add to ans string then return
    for i in freqs:
        ans += i[0] * i[1]
    return ans

print(frequency_sort("tree"))