import os
from pathlib import Path
from typing import Union


def format_path(path: Union[str, Path]) -> str:
    """
    Returns a string path and expanding the home directory if present.
    """
    return os.path.expanduser(path)
