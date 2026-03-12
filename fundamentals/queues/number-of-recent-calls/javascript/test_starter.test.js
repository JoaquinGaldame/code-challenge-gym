const { solve } = require("./starter");

test("recent calls example", () => {
  expect(solve([1, 100, 3001, 3002])).toEqual([1, 2, 3, 3]);
});

test("all calls fit window", () => {
  expect(solve([1000, 2000, 3000])).toEqual([1, 2, 3]);
});

test("old calls leave window", () => {
  expect(solve([1, 4000, 7000])).toEqual([1, 1, 2]);
});
