import os
from termcolor import cprint
import argparse
import subprocess


class RenameImages(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**self.kwargs)

    @property
    def exts_remove(self):
        """
        for data recovery, do not want these exts
        """
        return [
            '.dll',
            '.elf',
            '.h',
            '.c',
            '.pyc',
            '.py',
            '.jsp',
            '.sh',
            '.f',
            '.sqlite',
            '.ttf',
            '.ico',
            '_apisetstub',
            '.ogg',
            'elshyph_dll_mui',
            '_dll_mui',
            '.lnk',
            '.java',
            '.apple',
            '.pl',
            '.pm',
            '.ini',
            '.rpm',
            '.txt',
            '_dll',
            '_DLL',
            '_MUI',
            '_exe',
            '.mov',
            '.mbox',
            '.xml',
            '.xml.gz',
            '.html.gz',
            '.html']

    def post_recovery_rename(self):
        """
        dpath is disabled, please ref cli/image_rename.py for DPath
        """
        self.dpath = None
        return
        for path in self.dpath.keys():
            # if self.rename_path(path) is True:
            #    continue
            if 'ecup_dir' not in path:
                pass
            files = self.dpath.get(path)
            if not files:
                continue
            for afile in files:
                # self.rename_file(path, afile)
                self.handle_afile(path, afile)

    def rename_files_path(self, path):
        import glob
        # could be file or path?!
        files = glob.glob('{}/*'.format(path))
        from img.image_rename import ImageRename
        ren = ImageRename(**self.kwargs)
        for afile in files:
            cmds = ren.rename_move_file(afile)
            if not cmds:
                continue
            for items in cmds:
                cprint(items, 'blue')
                if self.ns.run:
                    subprocess.run(items)
            raise Exception('once for test')

    def handle_afile(self, path, afile):
        """
        move if identified, but do not remove
        """
        for ext in self.exts_remove:
            if afile.endswith(ext):
                afile = os.path.join(path, afile)
                print('skip but not remove {}'.format(afile))
                # os.remove(afile)
                return
        from img.image_rename import ImageRename
        ren = ImageRename(**self.kwargs)
        afile = os.path.join(path, afile)
        print(afile)
        if afile.endswith('.jpg'):
            ren.rename_move_file(afile)
        else:
            return
            print('skip as {} is not jpg'.format(afile))

    def rename(self, path):
        self.rename_files_path(path)
