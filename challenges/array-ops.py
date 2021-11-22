# Two arrays will be given as inputs
# array1: an array of distinct positive integers
# array2: an array of three kind of operations
#         operation type 1: [1,x] where x is a positive integer from 1 - infinity
#                           what to do? add x to each elements of  array1
#         operation type 2: [0,x]
#                         what to do? add x to the end of array1
#
#         operation tyoe 3: [2]
#                          what to do? find the lowest element of array1
#
# Note: the order of the operation matters, as the opertions can come in any order Any of the operations may be repeated, and may be
#       non-existent
#
#       Operation type 3 determines the final output. The initial output should be Zero.
#
#
# Example input 1 =[1,2,4,5,3], input 2 [[1,3],[0,3],[2]]
#              first operation [1,x] where x =3
#              therefore input1 changes to [4,5,7,8,6]
#              second operation [0,x] where x =3
#              therefore input1 changes to  [4,5,7,8,6,3]
#              third operation [2]
#              therefore out output is the minimum of [4,5,7,8,6,3] = 3
#
# Example using the same input 1 =[1,2,4,5,3], input 2 [[2],[1,3],[0,3],[2]]
#
#            in this case the output = 4
def solution(a, b):
    count = 0
    for i in b:
        if len(b) == 2:
            if i[0] == 1:
                a = [x+i[1] for x in a]
            elif i[0] == 2:
                a.append(i[1])
        else:
            count += min(a)
    return count

print(solution([1,2,4,5,3], [[1,3],[0,3],[2]]))