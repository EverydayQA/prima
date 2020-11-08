import argparse


class CliImageRename(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**self.kwargs)

    def rename(self):
        path = self.ns.path
        from data_recovery.img.rename_images import RenameImages
        ren = RenameImages(**self.kwargs)
        # ren.post_recovery_rename()
        ren.rename(path)
