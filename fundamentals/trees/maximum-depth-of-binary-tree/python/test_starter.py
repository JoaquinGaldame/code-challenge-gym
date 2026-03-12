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
    def test_balanced_tree(self):
        tree = {
            "val": 3,
            "left": {"val": 9, "left": None, "right": None},
            "right": {
                "val": 20,
                "left": {"val": 15, "left": None, "right": None},
                "right": {"val": 7, "left": None, "right": None},
            },
        }
        self.assertEqual(solve(tree), 3)

    def test_empty_tree(self):
        self.assertEqual(solve(None), 0)

    def test_unbalanced_tree(self):
        tree = {
            "val": 1,
            "left": {
                "val": 2,
                "left": {"val": 3, "left": None, "right": None},
                "right": None,
            },
            "right": None,
        }
        self.assertEqual(solve(tree), 3)


if __name__ == "__main__":
    unittest.main()
