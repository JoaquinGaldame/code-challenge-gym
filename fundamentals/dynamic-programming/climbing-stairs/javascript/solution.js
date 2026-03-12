function solve(data) {
  if (data <= 2) {
    return data;
  }

  let prev = 1;
  let curr = 2;

  for (let step = 3; step <= data; step += 1) {
    [prev, curr] = [curr, prev + curr];
  }

  return curr;
}

module.exports = { solve };
