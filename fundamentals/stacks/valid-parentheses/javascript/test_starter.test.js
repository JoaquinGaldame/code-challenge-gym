const { solve } = require("./starter");

test("valid sequence", () => {
  expect(solve("()[]{}")).toBe(true);
});

test("invalid order", () => {
  expect(solve("(]")).toBe(false);
});

test("unclosed opening bracket", () => {
  expect(solve("([" )).toBe(false);
});
