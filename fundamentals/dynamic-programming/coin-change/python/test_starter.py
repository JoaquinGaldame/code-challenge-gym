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
    def test_can_make_amount(self):
        self.assertEqual(solve({"coins": [1, 2, 5], "amount": 11}), 3)

    def test_amount_cannot_be_formed(self):
        self.assertEqual(solve({"coins": [2], "amount": 3}), -1)

    def test_zero_amount(self):
        self.assertEqual(solve({"coins": [1], "amount": 0}), 0)


if __name__ == "__main__":
    unittest.main()
