#!/bin/bash
set -e
set -x


# Check if sudo exists
sudo_exists=$(command -v sudo >/dev/null 2>&1 && echo true || echo false)

if [ "$sudo_exists" = true ]; then
    sudo apt install zsh -y
else
    apt install zsh -y
fi

# tmux
cd $HOME
rm -rf ~/.tmux
git clone https://github.com/gpakosz/.tmux.git ~/.tmux
ln -s -f .tmux/.tmux.conf

# oh-my-zsh
cd $HOME
rm -rf ~/.oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended


# Powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# fzf
rm -rf ~/.fzf
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install --all


# Download dotfiles from github
cd ~/.dotfiles
cp .zshrc ~/
cp .exports ~/
cp .funcs ~/
cp .aliases ~/
cp .tmux.conf.local ~/
