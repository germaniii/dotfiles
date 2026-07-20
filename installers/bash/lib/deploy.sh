DOTFILES_DIR="$HOME/dotfiles"
BACKUP_DIR="$HOME/.dotfiles-backup/$(date +%Y%m%d-%H%M%S)"

backup_file() {
    local target="$1"
    if [ -f "$target" ] || [ -L "$target" ] || [ -d "$target" ]; then
        mkdir -p "$BACKUP_DIR/$(dirname "${target#$HOME/}")"
        cp -P "$target" "$BACKUP_DIR/${target#$HOME/}" 2>/dev/null || true
        echo_info "Backed up $target"
    fi
}

deploy_directory() {
    local src_dir="$1"
    [ ! -d "$src_dir" ] && return
    local has_files
    has_files=$(find "$src_dir" -mindepth 1 -maxdepth 1 2>/dev/null | head -1)
    [ -z "$has_files" ] && return

    echo_step "Deploying from $(basename "$src_dir")..."
    find "$src_dir" -type f -o -type l | while IFS= read -r file; do
        local rel="${file#$src_dir/}"
        local dest="$HOME/$rel"
        backup_file "$dest"
    done
    cp -r "$src_dir/." "$HOME/" 2>/dev/null
    echo_ok "Deployed $(find "$src_dir" -type f | wc -l | tr -d ' ') files"
}

deploy_common() {
    deploy_directory "$DOTFILES_DIR/configs/common"
}

deploy_linux() {
    deploy_directory "$DOTFILES_DIR/configs/linux"
}

deploy_macos() {
    deploy_directory "$DOTFILES_DIR/configs/macos"
}

deploy_by_os() {
    deploy_common
    case "$OS" in
        macos) deploy_macos ;;
        linux) deploy_linux ;;
    esac
}
