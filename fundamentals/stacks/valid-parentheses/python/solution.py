def solve(data):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in data:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            return False

    return not stack
