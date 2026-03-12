const { solve } = require("./starter");

test("balanced tree", () => {
  const tree = {
    val: 3,
    left: { val: 9, left: null, right: null },
    right: {
      val: 20,
      left: { val: 15, left: null, right: null },
      right: { val: 7, left: null, right: null },
    },
  };

  expect(solve(tree)).toBe(3);
});

test("empty tree", () => {
  expect(solve(null)).toBe(0);
});

test("unbalanced tree", () => {
  const tree = {
    val: 1,
    left: {
      val: 2,
      left: { val: 3, left: null, right: null },
      right: null,
    },
    right: null,
  };

  expect(solve(tree)).toBe(3);
});
