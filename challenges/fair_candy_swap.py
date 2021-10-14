import copy

def fairCandySwap(aliceSizes, bobSizes):
    """
    :type aliceSizes: List[int]
    :type bobSizes: List[int]
    :rtype: List[int]
    """
    A = aliceSizes
    B = bobSizes
    difference = (sum(A) - sum(B)) // 2

    for candy in B:
        print(difference, candy)
        if difference + candy in A:
            return [difference + candy, candy]


print(fairCandySwap([1, 1], [2, 2]))
