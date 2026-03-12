const { solve } = require("./solution");

test("repeated pattern", () => {
  expect(solve("abcabcbb")).toBe(3);
});

test("all same character", () => {
  expect(solve("bbbbb")).toBe(1);
});

test("window must jump forward", () => {
  expect(solve("pwwkew")).toBe(3);
});
