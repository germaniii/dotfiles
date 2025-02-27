#
# ~/.bash_profile
#
tmux new-session -A -s germaniii
clear

[[ -f ~/.bashrc ]] && . ~/.bashrc

export MOZ_ENABLE_WAYLAND=1
export EDITOR=nvim
export VISUAL=nvim
export TERM=tmux-256color
export PS1="\u@\h \[\033[35m\]\w\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "
export PATH=~/Documents/Programs/bin:~/.nvm/versions/node/v18.20.3/bin:$PATH
export DISPLAY=:0
export EDITOR=nvim
export VISUAL=nvim
source /usr/share/nvm/init-nvm.sh
