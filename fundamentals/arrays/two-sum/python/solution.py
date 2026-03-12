def solve(data):
    nums = data["nums"]
    target = data["target"]
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    raise ValueError("Expected exactly one valid pair.")
