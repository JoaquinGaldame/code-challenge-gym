import importlib.util
from pathlib import Path
import unittest


def load_solve():
    solution_path = Path(__file__).with_name("solution.py")
    spec = importlib.util.spec_from_file_location("exercise_solution", solution_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.solve


solve = load_solve()


class SolutionTests(unittest.TestCase):
    def test_valid_anagram(self):
        self.assertTrue(solve({"s": "anagram", "t": "nagaram"}))

    def test_invalid_anagram(self):
        self.assertFalse(solve({"s": "rat", "t": "car"}))

    def test_same_letters_different_counts(self):
        self.assertFalse(solve({"s": "aacc", "t": "ccac"}))


if __name__ == "__main__":
    unittest.main()
