def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i, j = 0, 1
    while j < len(nums):
        if nums[i] == nums[j]:
            nums.pop(j)
        else:
            i = j
            j += 1

    return len(nums)

print(removeDuplicates([1,1,2]))