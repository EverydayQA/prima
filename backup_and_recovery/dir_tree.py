import os
import subprocess
from termcolor import cprint
from img.image_header_jpeg import ImageHeaderJpeg


class DPath(object):
    """
    Go through subdir to find proper files wanted with certain conditions
    files restored by photorec without proper file names
    """

    def __init__(self, path):
        self.path = path
        self.dpath = self.d_walk(self.path)

    def d_walk(self, rootdir):
        df = {}
        for path, subdirs, files in os.walk(rootdir):
            if files:
                df[path] = list(set(files))
        return df


class TreeInside(object):

    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.args = args
        self.kwargs = kwargs
        dp = DPath(path)
        self.dpath = dp.dpath

    def get_paths(self):
        return list(self.dpath.keys())


class TreeFromArgs(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.dpath = self.kwargs.get('dpath', {})

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

    def newname(self, name):
        if not name:
            return name
        name = name.replace('(', '')
        name = name.replace(')', '')
        name = name.replace('\'', '')
        name = name.replace('\"', '')
        name = name.replace(' ', '')
        name = name.replace('+', '')
        name = name.replace('[', '')
        name = name.replace(']', '')
        name = name.replace(',', '')
        name = name.replace(';', '')
        name = name.replace(':', '')
        name = name.replace('!', '')
        name = name.replace('\0', '')

        return name

    def newpath(self, path):
        basename = os.path.basename(path)
        newname = self.newname(basename)
        dirname = os.path.dirname(path)
        newpath = os.path.join(dirname, newname)
        return newpath

    def rename_file(self, path, afile):
        """
        same as rename_path()?
        """
        afile = os.path.join(path, afile)
        if not os.path.isfile(afile):
            cprint('skip missing file {}'.format(afile), 'red')
            return None
        newfile = self.newpath(afile)
        if newfile != afile:
            cmds = ['mv', afile, newfile]
            cprint(cmds, 'blue')
            # subprocess.call(cmds)
            return True
        return False

    def rename_path(self, path):
        if not os.path.isdir(path):
            cprint('skip missing path {}'.format(path), 'red')
            return None

        newpath = self.newpath(path)
        if newpath != path:
            cmds = ['mv', path, newpath]
            cprint(cmds, 'yellow')
            # subprocess.call(cmds)
            return True
        return False

    def post_recovery_rename(self):
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

    @property
    def dest(self):
        return '/shared/from_ausdesktop'

    def move_jpeg(self, afile, extra=None):
        """
        rename and move jpeg files
        """
        hdr = ImageHeaderJpeg()
        newname = hdr.get_newname(afile)
        cprint('move and rename {}'.format(afile), 'green')
        print(afile)
        print(newname)
        print(self.dest)
        if not newname:
            raise Exception('no newname')
        basename = os.path.basename(afile)
        newfile = '{}.{}'.format(newname, basename)
        newdir = os.path.join(self.dest, newname)
        newfile = os.path.join(newdir, newfile)
        print(newdir)
        print(newfile)
        cmds = ['mkdir', '-p', newdir]
        print(cmds)
        # subprocess.check_call(cmds)
        if not os.path.isdir(newdir):
            return
        if os.path.isfile(newfile):
            print(afile)
            print(newfile)
            raise Exception('newfile already exist')

        cmds = ['mv', '-v', afile, newfile]
        print(cmds)
        # subprocess.call(cmds)
        return

    def glob_jpgs(self, path):
        import glob
        files = glob.glob('{}/*.jpg'.format(path))
        for afile in files:
            self.move_jpeg(afile)

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
        afile = os.path.join(path, afile)
        print(afile)
        if afile.endswith('.jpg'):
            self.move_jpeg(afile)
        else:
            return
            print('skip as {} is not jpg'.format(afile))


def main():
    path = os.getcwd()
    dt = DPath(path)
    d = {}
    d['dpath'] = dt.dpath
    d['path'] = path
    d['dns'] = {}
    tf = TreeFromArgs(**d)
    # tf.post_recovery_rename()
    tf.glob_jpgs(path)


if __name__ == '__main__':
    main()
