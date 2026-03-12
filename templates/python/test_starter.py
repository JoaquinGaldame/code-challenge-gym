import importlib.util
from pathlib import Path
import unittest


def load_solve():
    starter_path = Path(__file__).with_name("starter.py")
    spec = importlib.util.spec_from_file_location("exercise_starter", starter_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.solve


solve = load_solve()


class StarterTests(unittest.TestCase):
    def test_replace_with_real_assertions(self):
        with self.assertRaises(NotImplementedError):
            solve([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
