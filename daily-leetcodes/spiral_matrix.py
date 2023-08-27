def spiral(arr):
    if not arr:
        return []

    rows, cols = len(arr), len(arr[0])
    result = []

    top, bottom, left, right = 0, rows - 1, 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse top
        for i in range(left, right + 1):
            result.append(arr[top][i])
        top += 1

        # Traverse right
        for i in range(top, bottom + 1):
            result.append(arr[i][right])
        right -= 1

        # Traverse bottom
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(arr[bottom][i])
            bottom -= 1

        # Traverse left
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(arr[i][left])
            left += 1

    spiral_result = []
    for i in range(0, len(result), cols):
        spiral_result.append(result[i:i + cols])

    for row in spiral_result:
        print(row)

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    spiral(arr)
