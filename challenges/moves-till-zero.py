# given an array of positive integer as an input e.g [1,0,9,8,0,1,0]
# perform the following tasks.
# given an array element iterate through the array and perform the following tasks
#
# (1) if a[i] = 0 move to the next element
# (2) if a[i] is greater than 0, subtract a[i] from a[i] and other subsequent elements:
#     note: only subtract if the subsequent elements  are greater than a[i]. if the any of the subsequent
#           elements are less that a[i], leaave it as it; if any of the subsequent elements are zero,
#           terminate the process and start the process again.
# (3) repeat the process till for example [1,4,0,7 ,8] becomes [0,0,0,0,0]. your output should be the addition of all the a[1]'s
#
# for example
#
# input [1,2,0,7,3,3,4,0] = 13
# input [0,0,0,0,0] = 0
# input [4, 4, 4, 4] = 4
# input [2,4,5,6,3,1] = 6
#
# step breakdown
# given an input a = [1,2,0,7,3,3,4,0]
# output at this point =0
# in this case our first a[i]
# 1st: a[i] = a[0] = 1
# output += a[i] = 0+1 = 1
# subtracting a[i] from a[i] and every subsequent array elements we get [(1-1),(2-1), 0, 7, 3, 3, 4, 0] = [0,1,0,7,3,3,4,0]
#
# 2nd a[i] = a[1] = 1
# output +=a[i] = 1 +1 =2
# subtracting a[i] from a[i] and every subsequent array elements we get [0,(1-1), 0, 7, 3, 3, 4, 0] = [0,0,0,7,3,3,4,0]
#
# 3rd a[i] = a[3] = 7
# output += a[i] = 2+7 = 9
# subtracting a[i] from a[i] and every subsequent array elements we get [0, 0, 0, (7-7), 3, 3, 4, 0] = [0,0,0,0,3,3,4,0]
#
# 4th a[i] = a[4] = 3
# output += a[i] = 9+3 = 12
# subtracting a[i] from a[i] and every subsequent array elements we get [0, 0, 0, 0, (3-3), (3-3), (4-3), 0] = [0,0,0,0,0,0,1,0]
#
# 5th a[i] = a[6] = 1
# output += a[i] = 12+1 = 13
# subtracting a[i] from a[i] and every subsequent array elements we get [0, 0, 0, 0, 0, 0, (1-1) , 0] = [0,0,0,0,0,0,0,0]
#
# finally there isnt any non-zero in the array, and the process ends.. output = 13

def solution(a):
    output = 0

    for i in range(len(a)):
        if a[i] != 0:
            output += a[i]
            current_number = a[i]
            for j in range(i, len(a)):
                if a[j] >= current_number:
                    a[j] -= current_number
                    print(a)
                elif a[j] == 0:
                    break
    return output

print(solution([1,2,0,7,3,3,4,0]))