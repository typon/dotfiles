#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse

def run_command(command):
    print(f"\033[34mExecuting command: {command}\033[0m")  # Print command in blue
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error details: {e}")
        sys.exit(1)

def check_command_exists(command):
    return subprocess.call(["which", command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def main():
    parser = argparse.ArgumentParser(description="Install script")
    parser.add_argument("--install-homebrew", action="store_true", help="Install Homebrew")
    parser.add_argument("--force-copy-dotfiles", action="store_true", help="Force copy dotfiles", default=True)
    args = parser.parse_args()

    # Check if zsh is installed
    if not check_command_exists("zsh"):
        print("zsh is not installed. Please install zsh before proceeding.")
        sys.exit(1)

    # Install Homebrew if requested and not already installed
    if args.install_homebrew and not check_command_exists("brew"):
        run_command('NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')

    # oh-my-zsh
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh")):
        run_command('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')

    # Powerlevel10k
    powerlevel10k_dir = os.path.expanduser("~/.oh-my-zsh/custom/themes/powerlevel10k")
    if not os.path.isdir(powerlevel10k_dir):
        run_command(f'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git {powerlevel10k_dir}')

    zsh_syntax_dir = os.path.expanduser("~/.oh-my-zsh/custom/plugins/fast-syntax-highlighting")
    print(f"Checking directory: {zsh_syntax_dir}")
    if not os.path.isdir(zsh_syntax_dir):
        print("Directory does not exist. Creating and cloning repository.")
        run_command(f'git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git "{zsh_syntax_dir}"')
    elif not os.listdir(zsh_syntax_dir):
        print("Directory exists but is empty. Cloning repository.")
        run_command(f'git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git "{zsh_syntax_dir}"')
    else:
        print("fast-syntax-highlighting directory already exists and is not empty. Skipping clone.")

    # Install tmux config
    tmux_dir = os.path.expanduser("~/.tmux")
    if not os.path.isdir(tmux_dir):
        run_command('git clone https://github.com/gpakosz/.tmux.git ~/.tmux')
        run_command('ln -s -f .tmux/.tmux.conf ~/.tmux.conf')

    # Download dotfiles from github
    os.chdir(os.path.expanduser("~/.dotfiles"))
    dotfiles = [".zshrc", ".exports", ".funcs", ".aliases", ".tmux.conf.local"]
    for file in dotfiles:
        if args.force_copy_dotfiles:
            copy_if_not_exists = "cp"
        else:
            copy_if_not_exists = "cp -n"
        run_command(f'{copy_if_not_exists} {file} ~/')

    exports_file = os.path.expanduser("~/.exports")
    if not os.path.exists(exports_file):
        print(f"Error: {exports_file} does not exist. Please create it before running this script.")
        sys.exit(1)
    
    # Add brew to PATH
    # brew's location is "/home/linuxbrew/.linuxbrew/bin/brew"
    os.environ['PATH'] = f"{os.environ['PATH']}:/home/linuxbrew/.linuxbrew/bin"

    # Install brew tools
    if args.install_homebrew and check_command_exists("brew"):
        brew_tools = ["eza", "bat", "ripgrep", "lazygit", "btop", "fzf", "neovim", "lazydocker", "git-delta", "knqyf263/pet/pet", "pueue", "glances"]
        run_command(f'brew install {" ".join(brew_tools)}')

    # Install kickstart nvim
    nvim_config_dir = os.path.expanduser("~/.config/nvim")
    if not os.path.isdir(nvim_config_dir):
        run_command(f'git clone https://github.com/nvim-lua/kickstart.nvim.git "{nvim_config_dir}"')

if __name__ == "__main__":
    main()

