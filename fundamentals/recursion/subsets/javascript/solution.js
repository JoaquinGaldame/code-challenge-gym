function solve(data) {
  const result = [];
  const subset = [];

  function backtrack(index) {
    if (index === data.length) {
      result.push([...subset]);
      return;
    }

    backtrack(index + 1);

    subset.push(data[index]);
    backtrack(index + 1);
    subset.pop();
  }

  backtrack(0);
  return result;
}

module.exports = { solve };
