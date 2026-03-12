function solve(data) {
  const queue = [];
  let left = 0;
  const counts = [];

  for (const ping of data) {
    queue.push(ping);
    while (queue[left] < ping - 3000) {
      left += 1;
    }
    counts.push(queue.length - left);
  }

  return counts;
}

module.exports = { solve };
