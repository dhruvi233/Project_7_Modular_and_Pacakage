"""Custom module for file operations."""

from pathlib import Path


def _safe_path(filename):
    """Check the filename before using it."""
    if not filename or not filename.strip():
        raise ValueError("File name cannot be empty.")

    path = Path(filename.strip())

    if path.is_absolute() or ".." in path.parts:
        raise ValueError("Please use a filename inside the project folder.")

    return path


def create_file(filename):
    """Create a new file without overwriting an existing file."""
    path = _safe_path(filename)

    with path.open("x", encoding="utf-8"):
        pass

    return path


def write_file(filename, content):
    """Write text to a file, replacing its previous contents."""
    path = _safe_path(filename)

    with path.open("w", encoding="utf-8") as file:
        file.write(content)

    return path


def read_file(filename):
    """Read and return the contents of a file."""
    path = _safe_path(filename)

    with path.open("r", encoding="utf-8") as file:
        return file.read()


def append_file(filename, content):
    """Append text to a file, creating it if it does not exist."""
    path = _safe_path(filename)

    with path.open("a", encoding="utf-8") as file:
        file.write(content)

        if content and not content.endswith("\n"):
            file.write("\n")

    return path
