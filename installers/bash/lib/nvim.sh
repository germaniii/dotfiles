install_nvim_config() {
    echo_title "Setting up Neovim configuration..."
    local nvim_dir="${XDG_CONFIG_HOME:-$HOME/.config}/nvim"
    if [ -d "$nvim_dir" ]; then
        backup_file "$nvim_dir"
        rm -rf "$nvim_dir"
    fi
    git clone -b germaniii https://github.com/germaniii/kickstart.nvim.git "$nvim_dir"
    echo_ok "Neovim config cloned to $nvim_dir"
}

install_mason_servers() {
    echo_title "Installing Mason LSP servers..."
    if command -v nvim &>/dev/null; then
        nvim --headless "+MasonInstall --all" +qa 2>/dev/null || true
        echo_ok "Mason packages installation triggered"
    else
        echo_warn "Neovim not installed, skipping Mason installation"
    fi
}
