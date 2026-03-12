function solve(data) {
  return new Set(data).size !== data.length;
}

module.exports = { solve };
