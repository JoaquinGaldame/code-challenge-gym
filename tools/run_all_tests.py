from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NPM_BIN = "npm.cmd" if sys.platform.startswith("win") else "npm"


def run_python(track: str, relative_path: str | None) -> int:
    patterns = []
    if relative_path:
        base = ROOT / relative_path
        if base.is_file():
            patterns = [base]
        else:
            patterns = sorted(base.rglob(f"test_{track}.py"))
    else:
        patterns = sorted(ROOT.glob(f"python/**/test_{track}.py")) + sorted(ROOT.glob(f"fundamentals/**/python/test_{track}.py"))

    for test_file in patterns:
        result = subprocess.run([sys.executable, str(test_file)], cwd=ROOT)
        if result.returncode != 0:
            return result.returncode
    return 0


def run_javascript(track: str, relative_path: str | None) -> int:
    if relative_path:
        base = ROOT / relative_path
        if base.is_file():
            test_files = [base]
        else:
            test_files = sorted(base.rglob(f"test_{track}.test.js"))

        if not test_files:
            return 0

        command = [NPM_BIN, "exec", "jest", "--", "--runInBand", "--runTestsByPath", *[str(path.relative_to(ROOT)) for path in test_files]]
        return subprocess.run(command, cwd=ROOT).returncode

    pattern = rf"test_{track}\.test\.js$"
    command = [NPM_BIN, "exec", "jest", "--", "--runInBand", f"--testPathPattern={pattern}"]
    return subprocess.run(command, cwd=ROOT).returncode


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecutar tests del repositorio.")
    parser.add_argument("--python", action="store_true", dest="python_only")
    parser.add_argument("--javascript", action="store_true", dest="javascript_only")
    parser.add_argument("--track", choices=["solution", "starter"], default="solution")
    parser.add_argument("--path", help="Ruta relativa a una carpeta o archivo de test concreto", default=None)
    args = parser.parse_args()

    run_python_tests = args.python_only or not args.javascript_only
    run_javascript_tests = args.javascript_only or not args.python_only

    if run_python_tests:
        code = run_python(args.track, args.path)
        if code != 0:
            raise SystemExit(code)

    if run_javascript_tests:
        code = run_javascript(args.track, args.path)
        if code != 0:
            raise SystemExit(code)


if __name__ == "__main__":
    main()
