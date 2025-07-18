#
# ~/.bashrc
#

# If not running interactively, don't do anything
stty -ixon # Prevent ranger from freezing

[[ $- != *i* ]] && return

[[ "$(whoami)" = "root" ]] && return

[[ -z "$FUNCNEST" ]] && export FUNCNEST=100          # limits recursive functions, see 'man bash'

## Use the up and down arrow keys for finding a command in history
## (you can write some initial letters of the command first).
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

################################################################################
## Some generally useful functions.
## Consider uncommenting aliases below to start using these functions.
##
## October 2021: removed many obsolete functions. If you still need them, please look at
## https://github.com/EndeavourOS-archive/EndeavourOS-archiso/raw/master/airootfs/etc/skel/.bashrc

_open_files_for_editing() {
    # Open any given document file(s) for editing (or just viewing).
    # Note1:
    #    - Do not use for executable files!
    # Note2:
    #    - Uses 'mime' bindings, so you may need to use
    #      e.g. a file manager to make proper file bindings.

    if [ -x /usr/bin/exo-open ] ; then
        echo "exo-open $@" >&2
        setsid exo-open "$@" >& /dev/null
        return
    fi
    if [ -x /usr/bin/xdg-open ] ; then
        for file in "$@" ; do
            echo "xdg-open $file" >&2
            setsid xdg-open "$file" >& /dev/null
        done
        return
    fi

    echo "$FUNCNAME: package 'xdg-utils' or 'exo' is required." >&2
}

####################################################################################
# Sources
####################################################################################

if [ -f ~/.bash_aliases ]; then
    . "$HOME/.bash_aliases"
fi

# All in one "Declarative" Package Manager
eval "$(mise activate bash)"
# Shell design
eval "$(starship init bash)"

# if [[ -z "$ZELLIJ" ]]; then
#     systemd-run --scope --user zellij attach --create "$(uname -n)"
# fi

# use ctrl-z to toggle in and out of bg (useful for vim bg)
if [[ $- == *i* ]]; then 
  stty susp undef
  bind '"\C-z":" fg\015"'
fi

####################################################################################
# Exports
####################################################################################

fastfetch
