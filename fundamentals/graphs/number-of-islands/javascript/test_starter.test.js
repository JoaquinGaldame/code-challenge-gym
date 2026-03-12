const { solve } = require("./starter");

test("multiple islands", () => {
  const grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
  ];

  expect(solve(grid)).toBe(3);
});

test("single island", () => {
  const grid = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"],
  ];

  expect(solve(grid)).toBe(1);
});

test("empty grid", () => {
  expect(solve([])).toBe(0);
});
