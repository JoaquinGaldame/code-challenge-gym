def solve(data):
    if not data:
        return 0

    min_price = data[0]
    best_profit = 0

    for price in data[1:]:
        if price < min_price:
            min_price = price
            continue
        best_profit = max(best_profit, price - min_price)

    return best_profit
