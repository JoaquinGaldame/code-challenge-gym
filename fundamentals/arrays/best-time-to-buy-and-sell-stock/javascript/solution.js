function solve(data) {
  if (data.length === 0) {
    return 0;
  }

  let minPrice = data[0];
  let bestProfit = 0;

  for (let index = 1; index < data.length; index += 1) {
    const price = data[index];
    if (price < minPrice) {
      minPrice = price;
      continue;
    }

    bestProfit = Math.max(bestProfit, price - minPrice);
  }

  return bestProfit;
}

module.exports = { solve };
