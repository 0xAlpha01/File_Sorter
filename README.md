# 📁 File Sorter

A simple Python CLI tool that automatically organizes files into folders based on their file types.

### ✨ Features

* Organizes Images, Documents, Videos, Audio, Archives, and Code
* Prevents duplicate files from being overwritten
* Supports `--dry-run` to preview changes
* Places unknown file types in `Other`

### 🚀 Usage

```bash
python file_sorter.py "C:\Users\USER\Downloads" --dry-run
```

If everything looks correct, remove `--dry-run`:

```bash
python file_sorter.py "C:\Users\USER\Downloads"
```

### 🐍 Requirements

* Python 3.x
* No external packages required

> Built to keep your folders clean, organized, and easy to manage.
