function solve(data) {
  if (data.length === 0 || data[0].length === 0) {
    return 0;
  }

  const rows = data.length;
  const cols = data[0].length;
  const visited = new Set();

  function key(row, col) {
    return `${row},${col}`;
  }

  function dfs(row, col) {
    const cellKey = key(row, col);
    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      data[row][col] !== "1" ||
      visited.has(cellKey)
    ) {
      return;
    }

    visited.add(cellKey);
    dfs(row + 1, col);
    dfs(row - 1, col);
    dfs(row, col + 1);
    dfs(row, col - 1);
  }

  let islands = 0;
  for (let row = 0; row < rows; row += 1) {
    for (let col = 0; col < cols; col += 1) {
      const cellKey = key(row, col);
      if (data[row][col] === "1" && !visited.has(cellKey)) {
        islands += 1;
        dfs(row, col);
      }
    }
  }

  return islands;
}

module.exports = { solve };
