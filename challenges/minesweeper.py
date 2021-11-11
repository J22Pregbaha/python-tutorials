# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a
# mine have a number in it that indicates the total number of mines in the neighboring cells.
# Starting off with some arrangement of mines we want to create a Minesweeper game setup.
def minesweeper(matrix):
    r = len(matrix)
    c = len(matrix[0])
    m = [[] for x in range(r)]
    for x in range(r):
        for y in range(c):
            count = 0
            if r > x - 1 >= 0 and c > y - 1 >= 0 and matrix[x - 1][y - 1]:
                count += 1
            if r > x >= 0 and c > y - 1 >= 0 and matrix[x][y - 1]:
                count += 1
            if r > x + 1 >= 0 and c > y - 1 >= 0 and matrix[x + 1][y - 1]:
                count += 1
            if r > x - 1 >= 0 and c > y >= 0 and matrix[x - 1][y]:
                count += 1
            if r > x + 1 >= 0 and c > y >= 0 and matrix[x + 1][y]:
                count += 1
            if r > x - 1 >= 0 and c > y + 1 >= 0 and matrix[x - 1][y + 1]:
                count += 1
            if r > x >= 0 and c > y + 1 >= 0 and matrix[x][y + 1]:
                count += 1
            if r > x + 1 >= 0 and c > y + 1 >= 0 and matrix[x + 1][y + 1]:
                count += 1
            m[x].append(count)
    return m

true = True
false = False
print(minesweeper([[true, false, false],
          [false, true, false],
          [false, false, false]]))