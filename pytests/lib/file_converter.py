import shutil


class FileConverter(object):

    def __init__(self, path_to_files):
        self._path_to_files = path_to_files

    def convert_files(self, rmv_src=False):
        self.doStuff()
        if rmv_src:
            shutil.rmtree(self._path_to_files)

    def doStuff(self):
        # does some stuff
        pass
