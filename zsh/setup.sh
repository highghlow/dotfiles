ln -s ${PWD}/zshrc ~/.zshrc
git clone https://github.com/ohmyzsh/ohmyzsh ~/.oh-my-zsh
rm -r ~/.oh-my-zsh/custom
ln -s ${PWD}/oh-my-zsh/custom ~/.oh-my-zsh/custom