from collections import deque

def explore_nodes(i, j, visited, grid):
    queue = deque()
    visited[i][j] = True
    queue.append((i, j))
    # print("queue",queue)

    # print("indexes", i, j)
    while len(queue) != 0:
        row = queue[0][0]
        column = queue[0][1]

        queue.popleft()
        # traverse all 8 directions
        # for x in range(-1, 2):
        #     for y in range(-1, 2):
        #
        #         new_row = row + x
        #         new_column = column + y
        #
        #         if 0 <= new_row < len(grid) and 0 <= new_column < len(
        #                 grid[0]) and visited[new_row][new_column] != True and grid[new_row][new_column] == "1":
        #             # print("new row and column to check", new_row, new_column)
        #

        #             visited[new_row][new_column] = True
        #             print("visited =>",new_row,new_column)
        #             print(visited)
        #             queue.append((new_row, new_column))

        # 4 directions traversal.
        # check_left()

        if 0 <= row < len(grid) and 0 <= column-1 < len(
                grid[0]) and visited[row][column-1] != True and grid[row][column-1] == "1":
            visited[row][column-1]= True
            queue.append((row, column-1))

        # check_right()
        if 0 <= row < len(grid) and 0 <= column+1 < len(
                grid[0]) and visited[row][column+1] != True and grid[row][column+1] == "1":
            visited[row][column+1]= True
            queue.append((row, column+1))


        # check_up()
        if 0 <= row-1 < len(grid) and 0 <= column < len(
                grid[0]) and visited[row-1][column] != True and grid[row-1][column] == "1":
            visited[row-1][column]= True
            queue.append((row-1, column))
        # check_down()
        if 0 <= row+1 < len(grid) and 0 <= column < len(
                grid[0]) and visited[row+1][column] != True and grid[row+1][column] == "1":
            visited[row+1][column]= True
            queue.append((row+1, column))


def start():
    # 4 side turns. no diagonals. ans: 1,3
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    #8 sides.
    # grid = [
    #     ["0","1"],
    #     ["1","0"],
    #     ["1","1"],
    #     ["1","0"]
    # ]
    # grid = [
    #     ["0","1","1","1","0","0","0"],
    #     ["0","0","1","1","0","1","0"]
    # ]
    islands = 0
    rows = len(grid)
    columns = len(grid[0])
    # print(rows,columns)
    visited = [["-1" for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if visited[i][j] != True and grid[i][j] == "1":
                print(i, j)
                islands += 1
                explore_nodes(i, j, visited, grid)

    print(islands)


start()
