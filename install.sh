#!/bin/bash
set -e
set -x

# Check if zsh is installed
if ! command -v zsh &> /dev/null
then
    echo "zsh is not installed. Please install zsh before proceeding."
    exit 1
fi

# Initialize arguments
install_homebrew=false

# Parse command line arguments
for arg in "$@"
do
    case $arg in
        --install-homebrew)
        install_homebrew=true
        shift # Remove argument from processing
        ;;
    esac
done

if [ "$install_homebrew" = true ]; then
     NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# oh-my-zsh
cd $HOME
rm -rf ~/.oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Install tmux config
cd $HOME
rm -rf ~/.tmux
git clone https://github.com/gpakosz/.tmux.git ~/.tmux
ln -s -f .tmux/.tmux.conf

# Download dotfiles from github
cd ~/.dotfiles
cp .zshrc ~/
cp .exports ~/
cp .funcs ~/
cp .aliases ~/
cp .tmux.conf.local ~/

source ~/.exports
# install brew tools
if [ "$install_homebrew" = true ]; then
    brew install eza bat ripgrep lazygit btop fzf neovim lazydocker git-delta knqyf263/pet/pet pueue glances
fi

# Install kickstart nvim
git clone https://github.com/nvim-lua/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim
