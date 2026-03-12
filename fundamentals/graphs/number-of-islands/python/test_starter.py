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
    def test_multiple_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(solve(grid), 3)

    def test_single_island(self):
        grid = [
            ["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"],
        ]
        self.assertEqual(solve(grid), 1)

    def test_empty_grid(self):
        self.assertEqual(solve([]), 0)


if __name__ == "__main__":
    unittest.main()
