# Several people are standing in a row and need to be divided into two teams.
# The first person goes into team 1, the second goes into team 2, the third goes into team 1 again,
# the fourth into team 2, and so on.
# You are given an array of positive integers - the weights of the people.
# Return an array of two integers, where the first element is the total weight of team 1,
# and the second element is the total weight of team 2 after the division is complete.
def alternatingSums(a):
    team1 = []
    team2 = []
    for index, element in enumerate(a):
        if index % 2 == 0:
            team1.append(element)
        else:
            team2.append(element)

    return [sum(team1), sum(team2)]

# OR

def alternatingSums2(a):
    return [sum(a[::2]), sum(a[1::2])]

print(alternatingSums2([50, 60, 60, 45, 70]))