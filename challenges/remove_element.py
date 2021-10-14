def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    j = 0
    while j < len(nums):
        if nums[j] == val:
            nums.pop(j)
        else:
            j += 1

    return len(nums)

print(removeElement([0,1,2,2,3,0,4,2], 2))