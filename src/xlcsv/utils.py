from pathlib import Path


def format_path(path: Path) -> Path:
    """
    Returns a string path and expanding the home directory if present.
    """
    return path.expanduser()
