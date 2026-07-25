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

# MACOS Specific
export BASH_SILENCE_DEPRECATION_WARNING=1
export OPENCODE_ENABLE_EXA=1

############################################################
# Unlimited history
############################################################
export HISTSIZE=
export HISTFILESIZE=

############################################################
# PATH
############################################################
export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:~/Documents/Programs/bin:~/.config/zellij:~/.local/bin:/opt/homebrew/opt/coreutils/libexec/gnubin:$PATH
export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"
export PATH="/opt/homebrew/opt/rustup/bin:$PATH"

[[ -f ~/.bashrc ]] && . ~/.bashrc
