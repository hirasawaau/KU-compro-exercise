from copy import deepcopy
from typing import List

grid1 = [['.','.','.','.','.','.'],
         ['.','o','o','.','.','.'],
         ['o','o','o','o','.','.'],
         ['o','o','o','o','o','.'],
         ['.','o','o','o','o','o'],
         ['o','o','o','o','o','.'],
         ['o','o','o','o','.','.'],
         ['.','o','o','.','.','.'],
         ['.','.','.','.','.','.']]
grid2 = [['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','o','.','o'],
         ['o','o','.','o','.','o','.'],
         ['o','o','o','o','o','.','.'],
         ['o','o','.','o','.','o','.'],
         ['.','.','.','.','o','.','o'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.']]
grid3 = [[' ',' ',' ',' ','o','o',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' '],
         [' ','o','o','o',' ',' ','o',' ',' ',' ','o'],
         ['o',' ',' ',' ','o',' ','o',' ',' ','o',' '],
         ['o',' ',' ',' ','o','o','o','o','o',' ',' '],
         ['o',' ',' ',' ','o',' ','o',' ',' ','o',' '],
         [' ','o','o','o',' ',' ','o',' ',' ',' ','o'],
         [' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ','o','o',' ',' ']]

def rotate_right(grid:List[List[str]]) -> List[List[str]]:
    newList:List[List[str]] = []
    for j in range(len(grid)):
        temList:List[str] = []
        for i in range(len(grid[i])):
            temList.append(grid[len(grid)-1-j][i])
        newList.append(temList)
        # print_grid(newList)
        # print('------------------')
    return newList

def rotate_left(grid:List[List[str]]) -> List[List[str]]:
    newList:List[List[str]] = []
    for j in range(len(grid)):
        temList = []
        for i in range(len(grid[i])):
            temList.append(grid[j][i])
        newList.append(temList)
    return newList

def print_grid(grid:List[List[str]]) -> None:
    for i in grid:
        for j in i:
            print(j , end="")
        print()

def rotate_180(grid:List[List[str]]) -> List[List[str]]:
    return rotate_right(rotate_right(grid))

def mirror(grid:List[List[str]]) -> List[List[str]]:
    mirrorGrid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            mirrorGrid[i][j] = grid[i][len(grid[i]) - 1 - j]
    return mirrorGrid