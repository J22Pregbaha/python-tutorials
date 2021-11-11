# Call two arms equally strong if the heaviest weights they each are able to lift are equal.
#
# Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left),
# and so are their weakest arms.
#
# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and min(yourLeft, yourRight) == min(friendsLeft, friendsRight)

# OR
def areEquallyStrong2(yourLeft, yourRight, friendsLeft, friendsRight):
    return sorted([yourLeft, yourRight]) == sorted([friendsLeft, friendsRight])

print(areEquallyStrong2(10, 15, 15, 10))