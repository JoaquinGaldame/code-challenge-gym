from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NPM_BIN = "npm.cmd" if sys.platform.startswith("win") else "npm"


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecutar un ejercicio puntual.")
    parser.add_argument("--language", choices=["python", "javascript"], required=True)
    parser.add_argument("--track", choices=["starter", "solution"], default="starter")
    parser.add_argument("--path", required=True, help="Ruta relativa a la carpeta del ejercicio")
    args = parser.parse_args()

    exercise_dir = ROOT / args.path
    if not exercise_dir.exists():
        raise SystemExit(f"No existe la ruta: {exercise_dir}")

    if args.language == "python":
        test_file = exercise_dir / f"test_{args.track}.py"
        raise SystemExit(subprocess.run([sys.executable, str(test_file)], cwd=ROOT).returncode)

    test_file = exercise_dir / f"test_{args.track}.test.js"
    relative_test = str(test_file.relative_to(ROOT))
    raise SystemExit(subprocess.run([NPM_BIN, "exec", "jest", "--", "--runInBand", "--runTestsByPath", relative_test], cwd=ROOT).returncode)


if __name__ == "__main__":
    main()
