function solve(data) {
  if (data === null) {
    return 0;
  }

  const leftDepth = solve(data.left);
  const rightDepth = solve(data.right);
  return 1 + Math.max(leftDepth, rightDepth);
}

module.exports = { solve };
