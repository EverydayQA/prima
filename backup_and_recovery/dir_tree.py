import os
import sys
import random
import subprocess
from pprint import pprint
from PIL import Image
from PIL.ExifTags import TAGS


class DirTree(object):
    """
    Go through subdir to find proper files wanted with certain conditions
    files restored by photorec without proper file names
    """

    def __init__(self, path):
        self.path = path
        self.dtree = self.d_walk(self.path)

    def d_walk(self, rootdir):
        df = {}
        for path, subdirs, files in os.walk(rootdir):
            if files:
                df[path] = list(set(files))
        return df

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

    def remove_exts(self):
        for path in self.dtree.keys():
            if 'ecup_dir' not in path:
                continue

            files = self.dtree.get(path)
            if not files:
                continue
            for afile in files:
                self.remove_file_with_ext(path, afile)
    @property
    def dest(self):
        return '/shared/from_ausdesktop'

    def move_file(self, afile, extra=None):
        dest = self.dest
        basename = os.path.basename(afile)
        items = basename.split('.')
        ext = items.pop()
        file_root = '.'.join(items)
        
        # avoid same file in different subdir
        newid = random.randrange(10000, 99999)
        if not extra:
            extra = random.randrange(100, 999)

        newfile = '{}.{}.{}.{}'.format(file_root, newid, extra, ext)
        dest = os.path.join(self.dest, newfile)
        print(dest)
        return
        cmds = ['mv', '-v', afile, dest]
        subprocess.call(cmds)

    def remove_file_with_ext(self, path, afile):
        for ext in self.exts_remove:
            if afile.endswith(ext):
                afile = os.path.join(path, afile)
                print('remove {}'.format(afile))
                os.remove(afile)
                return
        afile = os.path.join(path, afile)
        print(afile)

        if afile.endswith('.jpg'):
            d = get_exif(afile)
            pprint(d)
            cmds = ['file', afile]
            out = subprocess.check_output(cmds)
            out = out.decode("utf-8")
            pprint(out)
            print(afile)
            out = out.upper()
            if '2017' in out:
                print('found {}'.format(afile))
                self.move_file(afile, extra='2017')
                return
            if 'iPhone'.upper() in out:
                print('found {}'.format(afile))
                self.move_file(afile, exra='iphone')
                return


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    try:
        info = i._getexif()
        if not info:
            return {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        return ret
    except Exception as e:
        pprint(e)
        return {}
    return {}

def main():
    path = os.getcwd()
    path = '/shared/backup/'
    dt = DirTree(path)
    dt.remove_exts()


if __name__ == '__main__':
    main()
