const { solve } = require("./starter");

test("detects duplicate", () => {
  expect(solve([1, 2, 3, 1])).toBe(true);
});

test("returns false when all values are distinct", () => {
  expect(solve([1, 2, 3, 4])).toBe(false);
});

test("detects duplicate negative value", () => {
  expect(solve([-1, 0, -1])).toBe(true);
});
