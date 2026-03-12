function solve(data) {
  const { s, t } = data;
  if (s.length !== t.length) {
    return false;
  }

  const counts = new Map();

  for (const char of s) {
    counts.set(char, (counts.get(char) || 0) + 1);
  }

  for (const char of t) {
    if (!counts.has(char)) {
      return false;
    }

    const nextCount = counts.get(char) - 1;
    if (nextCount === 0) {
      counts.delete(char);
    } else {
      counts.set(char, nextCount);
    }
  }

  return counts.size === 0;
}

module.exports = { solve };
