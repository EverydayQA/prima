import os
from termcolor import cprint


class ImageRename(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.newpath = self.kwargs.get('newpath', None)
        self.path = self.kwargs.get('path', None)

    def new_basename(self, file_or_path):
        basename = os.path.basename(file_or_path)
        newname = self.newname(basename)
        dirname = os.path.dirname(file_or_path)
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
        newfile = self.new_basename(afile)
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

        newpath = self.new_basename(path)
        if newpath != path:
            cmds = ['mv', path, newpath]
            cprint(cmds, 'yellow')
            # subprocess.call(cmds)
            return True
        return False

    def cmds_make_newpath(self, newdir):
        if os.path.isdir(newdir):
            return []
        cmds = ['mkdir', '-p', newdir]
        return cmds

    def rename_move_file(self, afile, extra=None):
        """
        create subdir first in newpath
        mv file to newpath as newname
        """
        cmds_group = []
        from img.image_header_jpeg import ImageHeaderJpeg
        hdr = ImageHeaderJpeg()

        # newdir
        new_subdir = hdr.get_newname(afile, filename=False)
        print('<{}>'.format(afile))
        print('<{}>'.format(new_subdir))
        print('<{}>'.format(self.newpath))
        newdir = os.path.join(self.newpath, new_subdir)
        cmds = self.cmds_make_newpath(newdir)
        if cmds:
            cmds_group.append(tuple(cmds))

        # new filename
        newname = hdr.get_newname(afile, filename=True)
        basename = os.path.basename(afile)

        if not newname:
            raise Exception('no newname')
        newfile = '{}.{}'.format(newname, basename)
        newfile = os.path.join(newdir, newfile)
        cmds = self.cmds_move_file(afile, newfile)
        if cmds:
            cmds_group.append(tuple(cmds))
        return cmds_group

    def cmds_move_file(self, afile, newfile):
        if os.path.isfile(newfile):
            print(afile)
            print(newfile)
            raise Exception('newfile already exist')

        cmds = ['mv', '-v', afile, newfile]
        return cmds
