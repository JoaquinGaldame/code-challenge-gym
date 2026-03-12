const { solve } = require("./solution");

test("finds pair in basic case", () => {
  expect(solve({ nums: [2, 7, 11, 15], target: 9 })).toEqual([0, 1]);
});

test("finds pair with duplicate values", () => {
  expect(solve({ nums: [3, 3], target: 6 })).toEqual([0, 1]);
});

test("finds pair when answer is not first two values", () => {
  expect(solve({ nums: [1, 4, 6, 10], target: 11 })).toEqual([0, 3]);
});
