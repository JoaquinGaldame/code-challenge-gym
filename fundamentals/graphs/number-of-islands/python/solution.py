def solve(data):
    if not data or not data[0]:
        return 0

    rows = len(data)
    cols = len(data[0])
    visited = set()

    def dfs(row, col):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or data[row][col] != "1"
            or (row, col) in visited
        ):
            return

        visited.add((row, col))
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    islands = 0
    for row in range(rows):
        for col in range(cols):
            if data[row][col] == "1" and (row, col) not in visited:
                islands += 1
                dfs(row, col)

    return islands
