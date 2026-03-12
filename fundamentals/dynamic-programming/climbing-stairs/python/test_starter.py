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
    def test_small_example(self):
        self.assertEqual(solve(2), 2)

    def test_four_steps(self):
        self.assertEqual(solve(4), 5)

    def test_five_steps(self):
        self.assertEqual(solve(5), 8)


if __name__ == "__main__":
    unittest.main()
