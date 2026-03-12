const { solve } = require("./solution");

test("default reference behavior", () => {
  expect(solve([1, 2, 3])).toEqual([1, 2, 3]);
});
