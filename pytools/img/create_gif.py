import os


class CreateHtml(object):

    def create_html(self):
        print('create html')


class CreateGif(object):

    def gif_using_convert(self, pngs, gif):
        """
        2 pngs to a gif image using convert cmd
        """
        cmds = ['convert', '-delay', str(20), '-loop', str(0)]
        cmds.extend(pngs)
        cmds.append(gif)
        return cmds

    def cmds_add_text(self, img, txt):
        """
        using convert --gravity --annotate?
        or -draw
        """

        return []

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

    def create_gif(self):
        self.get_clipath()
        gif = self.get_output()
        cmds = self.gif_using_convert(self.files(), gif)
        print(cmds)
        import subprocess
        subprocess.check_output(cmds)
        self.create_html()


def main():
    cli = CreateGifCli()
    cli.create_gif()


if __name__ == '__main__':
    main()
