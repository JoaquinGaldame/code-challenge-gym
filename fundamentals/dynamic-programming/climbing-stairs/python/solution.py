def solve(data):
    if data <= 2:
        return data

    prev, curr = 1, 2
    for _ in range(3, data + 1):
        prev, curr = curr, prev + curr
    return curr
