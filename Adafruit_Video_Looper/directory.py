# Copyright 2015 Adafruit Industries.
# Author: Tony DiCola
# License: GNU GPLv2, see LICENSE.txt
import pyinotify


class MyEventHandler(pyinotify.ProcessEvent):
    ischanged = False

    def process_IN_CREATE(self, event):
        self.ischanged = True

    def process_IN_DELETE(self, event):
        self.ischanged = True

    def process_IN_MODIFY(self, event):
        self.ischanged = True

    def process_IN_MOVED_TO(self, event):
        self.ischanged = True

    def process_IN_MOVED_FROM(self, event):
        self.ischanged = True

class DirectoryReader(object):

    def __init__(self, config, extensions):
        """Create an instance of a file reader that just reads a single
        directory on disk.
        """
        self._load_config(config)
        self._ischanged = False
        # watch manager
        self.wm = pyinotify.WatchManager()
        self.mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY | pyinotify.IN_MOVED_TO | pyinotify.IN_MOVED_FROM
        self.wm.add_watch(self._path, self.mask)

        # event handler
        self.eh = MyEventHandler()

        # notifier
        self.notifier = pyinotify.ThreadedNotifier(self.wm, self.eh)
        self.notifier.start()

    def _load_config(self, config):
        self._path = config.get('directory', 'path')

    def search_paths(self):
        """Return a list of paths to search for files."""
        #vid_dirs = glob.glob(self._path + '*')
        #vid_dirs.extend(glob.glob(self._path + '*/*'))
        ## print vid_dirs
        #return vid_dirs
        return [self._path]

    def is_changed(self):
        """Return true if the file search paths have changed."""
        # For now just return false and assume the path never changes.  In the
        # future it might be interesting to watch for file changes and return
        # true if new files are added/removed from the directory.  This is 
        # called in a tight loop of the main program so it needs to be fast and
        # not resource intensive.

        return self.eh.ischanged

    def idle_message(self):
        """Return a message to display when idle and no files are found."""
        return 'No files found in {0}'.format(self._path)

    def reset(self):
        self.eh.ischanged = False
        return


def create_file_reader(config, extensions):
    """Create new file reader based on reading a directory on disk."""
    return DirectoryReader(config, extensions)
