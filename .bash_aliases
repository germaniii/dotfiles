####################################################################
# Aliases
####################################################################

alias vim=nvim
alias vidir="nvim -c 'Oil'"
alias edir="nvim -c 'Oil'"
alias ls='ls --color=auto'
alias ll='ls -lav --ignore=..'   # show long listing of all except ".."
alias l='ls -lav --ignore=.?*'   # show long listing but no hidden dotfiles except "."

####################################################################
# Functions
####################################################################

# Auto complete sample
function autoComp () {
    echo "auto comp $1"
}
function _autoComp () {
    local cur opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    opts="auto-answer mass-message scenario line-webhook backup-scenario"
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}
complete -F _autoComp autoComp

function updateMirrors () {
    reflector --verbose -l 200 -n 20 -p http --sort rate --save /etc/pacman.d/mirrorlist
}

function globalGitIgnore() {
    touch ~/.gitignore
    git config --global core.excludesFile '~/.gitignore'
}

function updateCloudflared(){
    sudo cloudflared service uninstall
    sudo rm /etc/cloudflared/config.yml
    sudo cloudflared --config $1 service install
}

function list-fonts(){
    fc-list | grep -i $1
}

function find() {
local files
  IFS=$'\n' files=($(fzf-tmux --query="$1" --multi --select-1 --exit-0))
  [[ -n "$files" ]] && vim "${files[@]}"
}

function drb(){
    docker compose down -v
    docker compose up --build
}

function dcup(){
    docker compose up
}

function dcp(){
    docker cp $1:$2 $3
}

function dcmd(){
    docker exec -it $1 ${@:2}
}

function mysql_connect () {
 sudo mysql -u root -pmysql2023 \
    -h $1 -P $2 
}
