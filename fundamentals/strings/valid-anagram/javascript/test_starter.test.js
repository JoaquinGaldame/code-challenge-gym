const { solve } = require("./starter");

test("valid anagram", () => {
  expect(solve({ s: "anagram", t: "nagaram" })).toBe(true);
});

test("invalid anagram", () => {
  expect(solve({ s: "rat", t: "car" })).toBe(false);
});

test("same letters different counts", () => {
  expect(solve({ s: "aacc", t: "ccac" })).toBe(false);
});
