

class CompileVim8(object):
    """
    For CentOs6 only, may or maynot work with fedora/rhel etc
    """

    def __init__(self, *args, **kwargs):
        pass

    @property
    def vi_cv_var_python_epfx(self):
        return 'vi_cv_var_python_epfx'

    def get_vi_cv_var_python_epfx(self):
        """
        If Python support is enabled, set this variable to the execution
        prefix of your Python interpreter (that is, where it thinks it is
        running).
        This is the output of the following Python script:
        import sys; print sys.exec_prefix
        """
        return None

    def vi_cv_var_python_pfx(self):
        return 'vi_cv_var_python_pfx'

    def get_vi_cv_var_python_pfx(self):
        """
        If Python support is enabled, set this variable to the prefix of your
        Python interpreter (that is, where it was installed).
        This is the output of the following Python script:
        import sys; print sys.prefix
        """
        return None

    def vi_cv_var_python_version(self):
        return 'vi_cv_var_python_version'

    def get_vi_cv_var_python_version(self):
        """
        If Python support is enabled, set this variable to the version of the
        Python interpreter that will be used.
        This is the output of the following Python script:
        import sys; print sys.version[:3]
        """
        return None

    def vi_cv_path_python_conf(self):
        return 'vi_cv_path_python_conf'

    def get_vi_cv_path_python_conf(self):
        """
        If Python support is enabled, set this variable to the path for
        Python's library implementation. This is a path like
        "/usr/lib/pythonX.Y/config" (the directory contains a file
        "config.c").
        """
        return None

    def cmds_yum_install(self):
        """
        https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source
        """
        cmd = 'sudo yum install -y ruby ruby-devel lua lua-devel luajit \
        luajit-devel ctags git python python-devel \
        python3 python3-devel tcl-devel \
        perl perl-devel perl-ExtUtils-ParseXS \
        perl-ExtUtils-XSpp perl-ExtUtils-CBuilder \
        perl-ExtUtils-Embed'
        cmds = cmd.split(' ')
        return cmds

    def vim_git_source(self):
        """
        cd ~
        git clone https://github.com/vim/vim.git
        """
        return 'https://github.com/vim/vim.git'

    def configure(self):
        """
        configure with env
        https://github.com/vim/vim/blob/master/src/INSTALLx.txt
        ac_cv_sizeof_int=4 \
        vim_cv_getcwd_broken=no \
        vim_cv_memmove_handles_overlap=yes \
        vim_cv_stat_ignores_slash=yes \
        vim_cv_tgetent=zero \
        vim_cv_terminfo=yes \
        vim_cv_toupper_broken=no \
        vim_cv_tty_group=world \
        ./configure \
        --build=i586-linux \
        --host=armeb-xscale-linux-gnu \
        --target=armeb-xscale-linux-gnu \
        --with-tlib=ncurses

        examples with python2.7
        ./configure --with-features=huge \
            --enable-multibyte \
        --enable-rubyinterp=yes \
        --enable-pythoninterp=yes \
        --with-python-config-dir=/usr/lib/python2.7/config \ # pay attention here check directory correct
        --enable-python3interp=yes \
        --with-python3-config-dir=/usr/lib/python3.5/config \
        --enable-perlinterp=yes \
        --enable-luainterp=yes \
            --enable-gui=gtk2 \
            --enable-cscope \
        --prefix=/tmp/vim8
        make
        make install
        """
        cmds = []
        return cmds
