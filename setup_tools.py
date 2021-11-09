import sys
from dataclasses import dataclass

@dataclass
class Context:
    step: int


def wait_for_enter():
    input("Press Enter to continue...")


def incr_step(ctx):
    ctx.step += 1
    return ctx


def install_kitty(ctx):
    print(f"Step {ctx.step}: Install kitty")
    print("curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin")
    wait_for_enter()
    ctx = incr_step(ctx)
    return ctx


def install_brew(ctx):
    print(f"Step {ctx.step}: Install Linuxbrew")
    print('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
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


if __name__ == "__main__":
    ctx = Context(step=0)

    steps = [
        install_kitty,
        install_brew,
        install_oh_my_zsh,
        install_powerlevel10k,
        install_zsh_syntax_highlighter,
        install_fzf,
        install_neovim,
    ]
    for step in steps:
         ctx = step(ctx)
