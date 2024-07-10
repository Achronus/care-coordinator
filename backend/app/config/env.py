from dotenv import load_dotenv
import os


def finder(target: str) -> str:
    """
    Searches for the `target` file by traversing up the directory tree from the current directory.

    Returns the path found or an empty string.
    """
    current_dir = os.getcwd()

    while True:
        potential_root = os.path.join(current_dir, target)
        if os.path.isfile(potential_root):
            return potential_root

        # Traverse up parent directory
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            # Reached root directory without finding
            return ""

        current_dir = parent_dir


def load_dotenv_file(filename: str) -> None:
    """Loads a dotenv file."""
    path = finder(filename)
    load_dotenv(path)
