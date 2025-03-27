#
# ~/.bash_profile
#
# tmux new-session -A -s germaniii
export MOZ_ENABLE_WAYLAND=1
export EDITOR=nvim
export VISUAL=nvim
export TERM=tmux-256color
export PS1="\u@\h \[\033[35m\]\w\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "
export PATH=~/Documents/Programs/bin:$PATH
export EDITOR=nvim
export VISUAL=nvim

# Unlimited history
export HISTSIZE=
export HISTFILESIZE=

[[ -f ~/.bashrc ]] && . ~/.bashrc
