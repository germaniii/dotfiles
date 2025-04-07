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
# Bash Colors
####################################################################
# Reset
Color_Off='\033[0m'       # Text Reset

# Regular Colors
Black='\033[0;30m'        # Black
Red='\033[0;31m'          # Red
Green='\033[0;32m'        # Green
Yellow='\033[0;33m'       # Yellow
Blue='\033[0;34m'         # Blue
Purple='\033[0;35m'       # Purple
Cyan='\033[0;36m'         # Cyan
White='\033[0;37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White

# Underline
UBlack='\033[4;30m'       # Black
URed='\033[4;31m'         # Red
UGreen='\033[4;32m'       # Green
UYellow='\033[4;33m'      # Yellow
UBlue='\033[4;34m'        # Blue
UPurple='\033[4;35m'      # Purple
UCyan='\033[4;36m'        # Cyan
UWhite='\033[4;37m'       # White

# Background
On_Black='\033[40m'       # Black
On_Red='\033[41m'         # Red
On_Green='\033[42m'       # Green
On_Yellow='\033[43m'      # Yellow
On_Blue='\033[44m'        # Blue
On_Purple='\033[45m'      # Purple
On_Cyan='\033[46m'        # Cyan
On_White='\033[47m'       # White

# High Intensity
IBlack='\033[0;90m'       # Black
IRed='\033[0;91m'         # Red
IGreen='\033[0;92m'       # Green
IYellow='\033[0;93m'      # Yellow
IBlue='\033[0;94m'        # Blue
IPurple='\033[0;95m'      # Purple
ICyan='\033[0;96m'        # Cyan
IWhite='\033[0;97m'       # White

# Bold High Intensity
BIBlack='\033[1;90m'      # Black
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIBlue='\033[1;94m'       # Blue
BIPurple='\033[1;95m'     # Purple
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White

# High Intensity backgrounds
On_IBlack='\033[0;100m'   # Black
On_IRed='\033[0;101m'     # Red
On_IGreen='\033[0;102m'   # Green
On_IYellow='\033[0;103m'  # Yellow
On_IBlue='\033[0;104m'    # Blue
On_IPurple='\033[0;105m'  # Purple
On_ICyan='\033[0;106m'    # Cyan
On_IWhite='\033[0;107m'   # White

####################################################################
# Functions
####################################################################

function ssh-forward () {
    # ssh -L localhost:8081:127.0.0.1:81 -N -f -p 22 <user>@<ip>
    ssh -L "localhost:$1:127.0.0.1:$1" -N -f -p 22 $2
}

function ssh-forward-show () {
    ps aux | grep ssh
}

function obsidian () {
    cd ~/vaults/personal
    git pull --rebase
    $EDITOR README.md
}

function obsidian-sync() {
    git pull --rebase --autostash
    git add .
    git commit -m "vault backup: $(date)"

    echo
    echo Your changes has been added to git.
    echo
    read -p "Would you like to push your changes? [Y/n]" choice

     if [[ "$choice" =~ ^[Nn]$ ]]; then
        echo "Skipping push."
        exit 0
    fi

     git push -u origin HEAD
}

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
    sudo reflector --verbose -l 20 -n 20 -p http --sort rate --save /etc/pacman.d/mirrorlist
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
