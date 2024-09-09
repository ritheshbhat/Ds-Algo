#https://takeuforward.org/data-structure/rotten-oranges-min-time-to-rot-all-oranges-bfs/
'''
Problem Statement: You will be given an m x n grid, where each cell has the following values :

2  –  represents a rotten orange
1  –  represents a Fresh orange
0  –  represents an Empty Cell
Every minute, if a Fresh Orange is adjacent to a Rotten Orange in 4-direction ( upward, downwards, right, and left ) it becomes Rotten.

Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it’s not possible, return
'''

from collections import deque
def traverse_grid_to_get_count_of_oranges(grid, rotten_oranges):
    fresh_oranges = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] ==2:
                rotten_oranges.append((i,j,0))
            elif grid[i][j] ==1:
                fresh_oranges+=1

    return fresh_oranges


def time_to_rot_all_oranges(grid):
    rotten_oranges= deque()
    fresh_oranges = traverse_grid_to_get_count_of_oranges(grid, rotten_oranges)

    directions = [(0,1),(1,0),(-1,0),(0,-1)] #right, up,down, left
    minutes = 0
    while rotten_oranges:
        row, column, minutes = rotten_oranges.popleft()

        for dr, dc in directions:
            new_row, new_column = row+dr, column+dc
            if 0 <=new_row < len(grid) and 0<= new_column <len(grid[0]) and grid[new_row][new_column] ==1:
                grid[new_row][new_column] =2
                rotten_oranges.append((new_row,new_column, minutes+1))
                fresh_oranges -=1

    return minutes if fresh_oranges ==0 else -1

if __name__=="__main__":
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(time_to_rot_all_oranges(grid))

    second_grid = [ [2,1,1] , [1,1,0] , [0,1,1] ]
    print(time_to_rot_all_oranges(second_grid))

    third_grid = [[]]