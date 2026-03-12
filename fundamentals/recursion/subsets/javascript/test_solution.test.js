const { solve } = require("./solution");

function normalize(subsets) {
  return subsets
    .map((subset) => [...subset].sort((a, b) => a - b))
    .sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
}

test("returns power set", () => {
  const expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]];
  expect(normalize(solve([1, 2, 3]))).toEqual(normalize(expected));
});

test("empty input", () => {
  expect(solve([])).toEqual([[]]);
});

test("single element", () => {
  expect(normalize(solve([9]))).toEqual(normalize([[], [9]]));
});
