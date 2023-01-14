def solve(matrix: list):
    rows = [-1] * len(matrix)
    cols = [-1] * len(matrix[0])
    print(rows, cols)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows[i] = 0
                cols[j] = 0

    for i in range(len(rows)):
        for j in range(len(cols)):
            if rows[i] == 0 or cols[j] == 0:
                matrix[i][j] = 0
    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 0],
        [5, 33, 1, 9],
        [7, 0, 9, 99]
    ]
    print(solve(matrix))
