const { solve } = require("./starter");

test("can make amount", () => {
  expect(solve({ coins: [1, 2, 5], amount: 11 })).toBe(3);
});

test("amount cannot be formed", () => {
  expect(solve({ coins: [2], amount: 3 })).toBe(-1);
});

test("zero amount", () => {
  expect(solve({ coins: [1], amount: 0 })).toBe(0);
});
