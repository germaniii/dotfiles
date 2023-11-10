alias vim=nvim
export EDITOR=nvim
export VISUAL=nvim
export g3pc=192.168.196.28

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


