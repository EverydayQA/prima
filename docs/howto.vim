vim 


Vundle howto
# clone to home directory
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# copy example section to ~/.vimrc
vim -o2 ~/.vim/bundle/Vundle.vim/README.md ~/.vimrc

# add extra plugins
.vimrc
" pep8 plugin
Plugin 'andviro/flake8-vim'
" jedi complete
Plugin 'davidhalter/jedi-vim'

