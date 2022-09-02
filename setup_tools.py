import sys
from dataclasses import dataclass

@dataclass
class Context:
    step: int


def wait_for_enter():
    input("Press Enter to continue...")
    print()


def incr_step(ctx):
    ctx.step += 1
    return ctx


def install_terminal_font(ctx):
    print(f"Step {ctx.step}: Install Jetbrains Mono Font")
    print("https://www.jetbrains.com/lp/mono/")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx


def install_kitty(ctx):
    print(f"Step {ctx.step}: Install kitty")
    print("curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def install_tmux_conf(ctx):
    print(f"Step {ctx.step}: Install tmux config")
    print("cd $HOME")
    print("git clone https://github.com/gpakosz/.tmux.git")
    print("ln -s -f .tmux/.tmux.conf")
    print("cp .tmux/.tmux.conf.local .")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def install_brew(ctx):
    print(f"Step {ctx.step}: Install Linuxbrew")
    print('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def install_zsh(ctx):
    print(f"Step {ctx.step}: Install zsh")
    print('sudo apt-get install zsh')
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def copy_zshrc(ctx):
    print(f"Step {ctx.step}: Copy zshrc from dotfiles repo")
    print("cp .zshrc $HOME/")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def copy_other_dotfiles(ctx):
    print(f"Step {ctx.step}: Copy other dotfiles")
    print("cp .exports $HOME/")
    print("cp .funcs $HOME/")
    print("cp .aliases $HOME/")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def install_oh_my_zsh(ctx):
    print(f"Step {ctx.step}: Install oh-my-zsh")
    print('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx


def install_powerlevel10k(ctx):
    print(f"Step {ctx.step}: Install powerlevel10k")
    print('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def install_zsh_syntax_highlighter(ctx):
    print(f"Step {ctx.step}: Install zsh syntax highligher")
    print('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting')
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx


def install_fzf(ctx):
    print(f"Step {ctx.step}: Install fzf")
    print("git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf")
    print("~/.fzf/install")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx


def install_neovim(ctx):
    print(f"Step {ctx.step}: Install neovim")
    print("brew install neovim")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def install_lazygit(ctx):
    print(f"Step {ctx.step}: Install lazygit")
    print("brew install lazygit")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx

def install_ripgrep(ctx):
    print(f"Step {ctx.step}: Install ripgrep")
    print("brew install ripgrep")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx


if __name__ == "__main__":
    ctx = Context(step=0)

    steps = [
        install_terminal_font,
        install_kitty,
        install_tmux_conf,
        install_brew,
        install_zsh,
        install_oh_my_zsh,
        copy_zshrc,
        copy_other_dotfiles,
        install_powerlevel10k,
        install_zsh_syntax_highlighter,
        install_fzf,
        install_neovim,
        install_lazygit,
        install_ripgrep,
    ]
    for step in steps:
         ctx = step(ctx)
