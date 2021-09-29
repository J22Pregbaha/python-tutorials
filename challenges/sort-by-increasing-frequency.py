from collections import Counter

def frequency_sort(nums):
    counts = Counter(nums)

    new_list = sorted(nums, key = lambda num: (counts[num], -num))
    print(counts)
    return new_list

print(frequency_sort([2,3,1,3,2]))