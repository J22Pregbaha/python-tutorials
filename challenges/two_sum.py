def twoSum(nums, target):
    for i, e in enumerate(nums):
        if target > 0:
            if e > target:
                continue
        else:
            if e < target:
                continue
        for index, char in enumerate(nums):
            if not i == index:
                total = e + char
                if total == target:
                    return [i, index]

print(twoSum([12, 2, 7, 11], 9))