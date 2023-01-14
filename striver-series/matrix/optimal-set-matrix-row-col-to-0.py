def solve(matrix: list):
    rows = len(matrix)
    columns = len(matrix[0])
    col0 = 1
    for i in range(rows):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1,columns):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    print("mat is", matrix)
    for i in range(1,rows):
        for j in range(1,columns):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

        if col0 == 0:
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 0],
        [5, 33, 1, 9],
        [7, 0, 9, 99]
    ]
    print(solve(matrix))
