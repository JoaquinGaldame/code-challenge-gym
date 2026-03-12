def solve(data):
    if data is None:
        return 0

    left_depth = solve(data.get("left"))
    right_depth = solve(data.get("right"))
    return 1 + max(left_depth, right_depth)
