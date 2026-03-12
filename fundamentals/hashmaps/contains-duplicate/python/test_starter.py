import importlib.util
from pathlib import Path
import unittest


def load_solve():
    solution_path = Path(__file__).with_name("starter.py")
    spec = importlib.util.spec_from_file_location("exercise_solution", solution_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.solve


solve = load_solve()


class SolutionTests(unittest.TestCase):
    def test_detects_duplicate(self):
        self.assertTrue(solve([1, 2, 3, 1]))

    def test_returns_false_when_all_values_are_distinct(self):
        self.assertFalse(solve([1, 2, 3, 4]))

    def test_detects_duplicate_negative_value(self):
        self.assertTrue(solve([-1, 0, -1]))


if __name__ == "__main__":
    unittest.main()
