const { solve } = require("./solution");

test("returns expected profit", () => {
  expect(solve([7, 1, 5, 3, 6, 4])).toBe(5);
});

test("returns zero when prices always fall", () => {
  expect(solve([7, 6, 4, 3, 1])).toBe(0);
});

test("handles short input", () => {
  expect(solve([5])).toBe(0);
});
