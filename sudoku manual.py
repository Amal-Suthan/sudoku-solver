import numpy as np

grid = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')
def possible(x,y,n):
    for i in range(0,9):
        if grid[i][x]==n and i != y:
            return False
        
    for i in range(0,9):
        if grid[y][i]==n and i != x:
            return False
    
    x0 = (x // 3) * 3
    y0 = (x // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 +3):
            if grid[Y][X] == n:
                return False

    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] ==0:
                for n in range(1,10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(grid)
    input('More?')
solve()