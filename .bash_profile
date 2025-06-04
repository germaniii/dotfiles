#
# ~/.bash_profile
#
[ -z "$TMUX" ] && exec tmux new-session -A -s "$USER@$HOSTNAME"

############################################################
# ENV Defaults
############################################################
export MOZ_ENABLE_WAYLAND=1
export EDITOR=nvim
export VISUAL=nvim
export TERM=tmux-256color

############################################################
# Unlimited history
############################################################
export HISTSIZE=
export HISTFILESIZE=

############################################################
# PATH
############################################################
export PATH=~/Documents/Programs/bin:~/.config/zellij:$PATH

[[ -f ~/.bashrc ]] && . ~/.bashrc

