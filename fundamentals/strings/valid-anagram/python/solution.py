from collections import Counter


def solve(data):
    return Counter(data["s"]) == Counter(data["t"])
