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
    def normalize(self, subsets):
        return sorted(sorted(item) for item in subsets)

    def test_returns_power_set(self):
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(self.normalize(solve([1, 2, 3])), self.normalize(expected))

    def test_empty_input(self):
        self.assertEqual(solve([]), [[]])

    def test_single_element(self):
        self.assertEqual(self.normalize(solve([9])), self.normalize([[], [9]]))


if __name__ == "__main__":
    unittest.main()
