# Copyright 2015 Adafruit Industries.
# Author: Tony DiCola
# License: GNU GPLv2, see LICENSE.txt
import os

class DirectoryReader(object):

    def __init__(self, config, extensions):
        """Create an instance of a file reader that just reads a single
        directory on disk.
        """
        self._mtimes = {}
        self._extensions = extensions
        self._load_config(config)

    def _load_config(self, config):
        self._path = config.get('directory', 'path')
        for path in os.listdir(self._path):
            self._mtimes[path] = os.path.getmtime(path)
            print(path + " " + self._mtimes[path])

    def search_paths(self):
        """Return a list of paths to search for files."""
        return [self._path]

    def is_changed(self):
        """Return true if the file search paths have changed."""
        # For now just return false and assume the path never changes.  In the
        # future it might be interesting to watch for file changes and return
        # true if new files are added/removed from the directory.  This is 
        # called in a tight loop of the main program so it needs to be fast and
        # not resource intensive.
        for path in os.listdir(self._path()):
            if path in self._mtimes:
                if self._mtimes.get(path) != os.path.getmtime(path):
                    return True
        return False

    def idle_message(self):
        """Return a message to display when idle and no files are found."""
        return 'No files found in {0}'.format(self._path)


def create_file_reader(config, extensions):
    """Create new file reader based on reading a directory on disk."""
    return DirectoryReader(config, extensions)
