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



def rotate_right(grid:List[List[str]]) -> List[List[str]]:
    newList:List[List[str]] = []
    for i in range(len(grid[0])):
        temList:List[str] = []
        for j in range(len(grid)):
            temList.append(grid[len(grid)-1-j][i])
        newList.append(temList)
        # print_grid(newList)
        # print('------------------')
    return newList

def rotate_left(grid:List[List[str]]) -> List[List[str]]:
    newList:List[List[str]] = []
    for i in range(len(grid[0])):
        temList = []
        for j in range(len(grid)):
            temList.append(grid[j][i])
        newList.append(temList)
    return newList

def print_grid(grid:List[List[str]]) -> None:
    for i in grid:
        for j in i:
            print(j , end="")
        print()

print_grid(grid1)
print('###########')
print_grid(rotate_right(grid1))
print('###########')
print_grid(rotate_right(rotate_right(grid1)))