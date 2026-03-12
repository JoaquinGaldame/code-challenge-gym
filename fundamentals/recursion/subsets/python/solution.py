def solve(data):
    result = []
    subset = []

    def backtrack(index):
        if index == len(data):
            result.append(subset[:])
            return

        backtrack(index + 1)

        subset.append(data[index])
        backtrack(index + 1)
        subset.pop()

    backtrack(0)
    return result
