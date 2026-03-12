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
    def test_recent_calls_example(self):
        self.assertEqual(solve([1, 100, 3001, 3002]), [1, 2, 3, 3])

    def test_all_calls_fit_window(self):
        self.assertEqual(solve([1000, 2000, 3000]), [1, 2, 3])

    def test_old_calls_leave_window(self):
        self.assertEqual(solve([1, 4000, 7000]), [1, 1, 2])


if __name__ == "__main__":
    unittest.main()
