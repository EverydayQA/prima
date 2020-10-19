import os


class CreateHtml(object):

    def create_html(self):
        print('create html')


class ImageMagic(object):
    GRAVITY = '-gravity'
    POINTSIZE = '-pointsize'
    DELAY = '-delay'
    ANNOTATE = '-annotate'
    DRAW = '-draw'
    FONT = '-font'
    FILL = '-fill'
    CONVERT = 'convert'


class CreateGif(ImageMagic):

    def gif_using_convert(self, pngs, gif):
        """
        2 pngs to a gif image using convert cmd
        """
        cmds = ['convert', '-delay', str(20), '-loop', str(0)]
        cmds.extend(pngs)
        cmds.append(gif)
        return cmds

    def cmds_add_text(self, img, img2, txt):
        """
        using convert --gravity --annotate?
        or -draw
        """
        cmds = [self.CONVERT, img, self.GRAVITY, 'Center', self.POINTSIZE, str(30),  self.ANNOTATE,  str(0), txt, img2]
        return cmds

    def cmds_draw_text(self, img, img2, txt):
        """
        text 300(from left),600(from top)
        """
        cmds = [self.CONVERT, self.FONT, 'helvetica', self.POINTSIZE, str(40), self.FILL, 'blue', self.DRAW, "text 600,600 '{}'".format(txt), img, img2]
        return cmds

    def gif_using_ffmpeg(self, pngs, gif):
        pass

    def todo(self):
        """
        3d image movie first, then gif?
        mincpik to make slice29.png
        """
        print('create html')


class CreateGifCli(CreateGif, CreateHtml):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.inputdir = self.get_clipath()

    def get_clipath(self):
        filepath = os.path.dirname(os.path.abspath(__file__))
        return filepath

    def get_output(self):
        gif = '/tmp/test.gif'
        print(gif)
        return gif

    def jpgs(self):
        return ['unknown.jpg', 'butter_fly.jpg']

    def files(self):
        files = []
        for img in self.jpgs():
            img = os.path.join(self.inputdir, img)
            files.append(img)
        return files

    def add_txt(self, img):
        basename = os.path.basename(img)
        img2 = os.path.join('/tmp', basename)
        basename = basename.replace('.', '')
        cmds = self.cmds_add_text(img, img2, basename)
        cmd = ' '.join(cmds)
        print(cmd)

        import subprocess
        subprocess.check_output(cmds)
        return img2

    def get_files_with_txt(self):
        files = []
        for img in self.files():
            img2 = self.add_txt(img)
            files.append(img2)
        return files

    def create_gif(self):
        self.get_clipath()
        gif = self.get_output()

        files = self.get_files_with_txt()
        cmds = self.gif_using_convert(files, gif)
        print(cmds)
        import subprocess
        subprocess.check_output(cmds)
        self.create_html()
        print(gif)


def main():
    cli = CreateGifCli()
    cli.create_gif()


if __name__ == '__main__':
    main()
