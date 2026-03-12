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
    def test_returns_expected_profit(self):
        self.assertEqual(solve([7, 1, 5, 3, 6, 4]), 5)

    def test_returns_zero_when_prices_always_fall(self):
        self.assertEqual(solve([7, 6, 4, 3, 1]), 0)

    def test_handles_short_input(self):
        self.assertEqual(solve([5]), 0)


if __name__ == "__main__":
    unittest.main()
