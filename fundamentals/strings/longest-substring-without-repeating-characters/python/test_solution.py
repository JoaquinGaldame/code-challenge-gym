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
    def test_repeated_pattern(self):
        self.assertEqual(solve("abcabcbb"), 3)

    def test_all_same_character(self):
        self.assertEqual(solve("bbbbb"), 1)

    def test_window_must_jump_forward(self):
        self.assertEqual(solve("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
