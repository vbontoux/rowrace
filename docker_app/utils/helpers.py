from pathlib import Path

class Helpers():

    def remove_directory_tree(self, start_directory):
        """Recursively and permanently removes the specified directory, all of its
        subdirectories, and every file contained in any of those folders."""
        start_directory = Path(start_directory)
        for path in start_directory.iterdir():
            if path.is_file():
                path.unlink()
            else:
                self.remove_directory_tree(path)
        start_directory.rmdir()