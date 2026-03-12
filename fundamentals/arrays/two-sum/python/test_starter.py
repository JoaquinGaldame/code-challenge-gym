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
    def test_finds_pair_in_basic_case(self):
        self.assertEqual(solve({"nums": [2, 7, 11, 15], "target": 9}), [0, 1])

    def test_finds_pair_with_duplicate_values(self):
        self.assertEqual(solve({"nums": [3, 3], "target": 6}), [0, 1])

    def test_finds_pair_when_answer_is_not_first_two_values(self):
        self.assertEqual(solve({"nums": [1, 4, 6, 10], "target": 11}), [0, 3])


if __name__ == "__main__":
    unittest.main()
