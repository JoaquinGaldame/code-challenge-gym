const { solve } = require("./starter");

test("returns the provided data by default", () => {
  expect(solve([1, 2, 3])).toEqual([1, 2, 3]);
});
