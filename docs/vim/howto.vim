
# flake8-vim is for syntax checking
version 8.2.348
Python 3.6.10 |Anaconda, Inc.| (default, Mar 23 2020, 23:13:11) 
or python v3.7.2
uname -r
5.5.10-100.fc30.x86_64

Error detected while processing function <SNR>42_init_py_modules:
line   27:
~/.vim/bundle/flake8-vim/ftplugin/python/pycodestyle/pycodestyle.py:112: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')

# how to fix the error, it is the REGEX again
~/.vim/bundle/flake8-vim/ftplugin/python/pycodestyle/pycodestyle.py
# EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[\[({] | [\]}),;:]')

git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# autocomplete
OMNI - is outdated?
jedi-vim easier to make it to work

has been issue with youcompleteme, but will try
current vim version is 8.1.1991, but 8.1.2269+ required
compile newer version of vim? 
sudo dnf update vim
YCM works on fedora 30
