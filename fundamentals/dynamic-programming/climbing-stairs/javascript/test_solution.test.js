const { solve } = require("./solution");

test("small example", () => {
  expect(solve(2)).toBe(2);
});

test("four steps", () => {
  expect(solve(4)).toBe(5);
});

test("five steps", () => {
  expect(solve(5)).toBe(8);
});
