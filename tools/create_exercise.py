from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates"
VALID_LEVELS = {"beginner", "intermediate", "advanced"}


def slugify(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def copy_tree(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=False)
    for entry in src.iterdir():
        target = dst / entry.name
        if entry.is_dir():
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)


def main() -> None:
    parser = argparse.ArgumentParser(description="Crear un ejercicio nuevo a partir de templates.")
    parser.add_argument("--language", choices=["python", "javascript"], required=True)
    parser.add_argument("--level", choices=sorted(VALID_LEVELS), required=True)
    parser.add_argument("--name", required=True, help="Nombre legible del ejercicio")
    args = parser.parse_args()

    slug = slugify(args.name)
    base_dir = ROOT / args.language / args.level
    existing = sorted([p for p in base_dir.iterdir() if p.is_dir()])
    next_index = len(existing) + 1
    folder_name = f"{next_index:02d}_{slug}"
    target_dir = base_dir / folder_name

    template_dir = TEMPLATE_ROOT / args.language
    copy_tree(template_dir, target_dir)

    problem_md = target_dir / "problem.md"
    content = problem_md.read_text(encoding="utf-8")
    problem_md.write_text(content.replace("Exercise Title", args.name.title()), encoding="utf-8")

    print(f"Creado: {target_dir}")


if __name__ == "__main__":
    main()
