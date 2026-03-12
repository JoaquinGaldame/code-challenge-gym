from collections import deque


def solve(data):
    recent = deque()
    counts = []

    for ping in data:
        recent.append(ping)
        while recent and recent[0] < ping - 3000:
            recent.popleft()
        counts.append(len(recent))

    return counts
