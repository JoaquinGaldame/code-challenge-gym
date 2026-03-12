function solve(data) {
  const pairs = new Map([
    [")", "("],
    ["]", "["],
    ["}", "{"],
  ]);
  const openings = new Set(["(", "[", "{"]);
  const stack = [];

  for (const char of data) {
    if (openings.has(char)) {
      stack.push(char);
      continue;
    }

    if (!pairs.has(char)) {
      return false;
    }

    if (stack.length === 0 || stack.pop() !== pairs.get(char)) {
      return false;
    }
  }

  return stack.length === 0;
}

module.exports = { solve };
