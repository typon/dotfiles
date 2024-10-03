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

if [ "$install_homebrew" = true ] && ! command -v brew &> /dev/null; then
     NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# oh-my-zsh
if [ ! -d "$HOME/.oh-my-zsh" ]; then
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
fi

# Powerlevel10k
if [ ! -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" ]; then
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
fi

# zsh-syntax-highlighting
zsh_syntax_dir="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
echo "Checking directory: $zsh_syntax_dir"

if [ ! -d "$zsh_syntax_dir" ]; then
    echo "Directory does not exist. Creating and cloning repository."
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$zsh_syntax_dir"
elif [ -z "$(ls -A "$zsh_syntax_dir")" ]; then
    echo "Directory exists but is empty. Cloning repository."
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$zsh_syntax_dir"
else
    echo "zsh-syntax-highlighting directory already exists and is not empty. Skipping clone."
fi

# Install tmux config
if [ ! -d "$HOME/.tmux" ]; then
    git clone https://github.com/gpakosz/.tmux.git ~/.tmux
    ln -s -f .tmux/.tmux.conf ~/.tmux.conf
fi

# Download dotfiles from github
cd ~/.dotfiles
cp -n .zshrc ~/
cp -n .exports ~/
cp -n .funcs ~/
cp -n .aliases ~/
cp -n .tmux.conf.local ~/

source ~/.exports
# install brew tools
if [ "$install_homebrew" = true ] && command -v brew &> /dev/null; then
    brew install eza bat ripgrep lazygit btop fzf neovim lazydocker git-delta knqyf263/pet/pet pueue glances
fi

# Install kickstart nvim
if [ ! -d "${XDG_CONFIG_HOME:-$HOME/.config}/nvim" ]; then
    git clone https://github.com/nvim-lua/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim
fi
