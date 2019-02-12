import numpy as np


def repeat_check(sudoku_grid, location): #checks if given column has same value more than once at given sudoku grid
    Y, X, y, x = location
    return((len(np.argwhere(sudoku_grid[Y, :, y, :] == sudoku_grid[Y, X, y, x]))) > 1 or
           (len(np.argwhere(sudoku_grid[:, X, :, x] == sudoku_grid[Y, X, y, x]))) > 1 or
           (len(np.argwhere(sudoku_grid[Y, X, :, :] == sudoku_grid[Y, X, y, x]))) > 1
           )


m = np.zeros((3, 3, 3, 3))  # Y, X, y, x

m[0, 1, 0, 0] = 2
m[0, 1, 0, 1] = 6
m[0, 2, 0, 0] = 7
m[0, 2, 0, 2] = 1
m[0, 0, 1, 0] = 6
m[0, 0, 1, 1] = 8
m[0, 1, 1, 1] = 7
m[0, 2, 1, 1] = 9
m[0, 0, 2, 0] = 1
m[0, 0, 2, 1] = 9
m[0, 1, 2, 2] = 4
m[0, 2, 2, 0] = 5
m[1, 0, 0, 0] = 8
m[1, 0, 0, 1] = 2
m[1, 1, 0, 0] = 1
m[1, 2, 0, 1] = 4
m[1, 0, 1, 2] = 4
m[1, 1, 1, 0] = 6
m[1, 1, 1, 2] = 2
m[1, 2, 1, 0] = 9
m[1, 0, 2, 1] = 5
m[1, 1, 2, 2] = 3
m[1, 2, 2, 1] = 2
m[1, 2, 2, 2] = 8
m[2, 0, 0, 2] = 9
m[2, 1, 0, 0] = 3
m[2, 2, 0, 1] = 7
m[2, 2, 0, 2] = 4
m[2, 0, 1, 1] = 4
m[2, 1, 1, 1] = 5
m[2, 2, 1, 1] = 3
m[2, 2, 1, 2] = 6
m[2, 0, 2, 0] = 7
m[2, 0, 2, 2] = 3
m[2, 1, 2, 1] = 1
m[2, 1, 2, 2] = 8

print(m)
print(repeat_check(m, [1, 0, 0, 0]))
