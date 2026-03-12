
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
    def test_identity_example(self):
        self.assertEqual(solve([1, 2, 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
