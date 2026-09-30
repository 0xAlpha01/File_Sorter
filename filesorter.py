#!/usr/bin/env python3
"""file-sorter: move files in a folder into subfolders by type.
Usage:
    python file_sorter.py ~/Downloads            # sort the folder
    python file_sorter.py ~/Downloads --dry-run  # preview only
"""
import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Audio": {".mp3", ".wav", ".flac", ".m4a"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".js", ".ts", ".go", ".html", ".css", ".json"},
}


def category_for(path: Path) -> str:
    ext = path.suffix.lower()
    for name, extensions in CATEGORIES.items():
        if ext in extensions:
            return name
    return "Other"


def unique_target(target: Path) -> Path:
    """Avoid overwriting: photo.png -> photo (1).png"""
    counter = 1
    candidate = target
    while candidate.exists():
        candidate = target.with_name(f"{target.stem} ({counter}){target.suffix}")
        counter += 1
    return candidate


def sort_folder(folder: Path, dry_run: bool = False) -> None:
    moved = 0
    for item in folder.iterdir():
        if not item.is_file() or item.name.startswith("."):
            continue
        dest_dir = folder / category_for(item)
        target = unique_target(dest_dir / item.name)
        print(f"{item.name}  ->  {dest_dir.name}/{target.name}")
        if not dry_run:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))
        moved += 1
    print(f"\n{'Would move' if dry_run else 'Moved'} {moved} file(s).")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sort files into folders by type.")
    parser.add_argument("folder", type=Path, help="Folder to sort")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving")
    args = parser.parse_args()

    if not args.folder.is_dir():
        parser.error(f"'{args.folder}' is not a folder")
    sort_folder(args.folder, args.dry_run)


if __name__ == "__main__":
    main()
