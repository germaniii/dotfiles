#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "$SCRIPT_DIR/lib/detect.sh"
source "$SCRIPT_DIR/lib/colors.sh"
source "$SCRIPT_DIR/lib/wizard.sh"
source "$SCRIPT_DIR/lib/packages.sh"
source "$SCRIPT_DIR/lib/deploy.sh"
source "$SCRIPT_DIR/lib/nvim.sh"
source "$SCRIPT_DIR/packages/base.sh"

if ! command -v dialog &>/dev/null && ! command -v whiptail &>/dev/null; then
    echo "Error: This installer requires 'dialog' or 'whiptail'."
    echo "Run the setup.sh bootstrap script which installs it automatically:"
    echo "  curl -fsSL https://raw.githubusercontent.com/germaniii/dotfiles/main/setup.sh | sh"
    exit 1
fi

SELECTED_PACKAGES=()
SELECTED_DE="NONE"

# --- Welcome ---

welcome() {
    wizard_infobox "Welcome" "Dotfiles Setup Wizard\n\nDetecting your system..."
    echo_title "Dotfiles Setup Wizard"
    echo_info "OS: ${BOLD}$OS${RESET}"
    if [ "$OS" = "linux" ]; then
        echo_info "Distro: ${BOLD}$DISTRO${RESET}"
    fi
    echo_info "Package Manager: ${BOLD}$PKG_MANAGER${RESET}"
    echo_info "Dialog: ${BOLD}$DIALOG_CMD${RESET}"
    echo

    if [ ! -t 0 ]; then
        echo_err "Cannot run interactively (not a terminal)"
        exit 1
    fi

    wizard_msgbox "System Detected" "OS: $OS${DISTRO:+ ($DISTRO)}\nPackage Manager: $PKG_MANAGER\n\nPress OK to continue."
}

# --- Desktop Environment Selection (Linux only) ---

select_de() {
    [ "$OS" != "linux" ] && return
    local items=()
    for choice in "${DE_CHOICES[@]}"; do
        local name desc selected
        name=$(echo "$choice" | cut -d'|' -f1)
        desc=$(echo "$choice" | cut -d'|' -f2)
        selected=$(echo "$choice" | cut -d'|' -f3)
        local help_text=""
        if [ "$name" != "NONE" ]; then
            local de_arr="DE_$name"
            local -n de_array="$de_arr"
            local pkgs=()
            for pkg_entry in "${de_array[@]}"; do
                pkgs+=("$(pkg_virtual_name "$pkg_entry")")
            done
            local IFS=','
            help_text="Includes: ${pkgs[*]}"
            unset IFS
        fi
        items+=("$name" "$desc" "$selected" "$help_text")
    done

    local result
    result=$(wizard_radiolist_help "Desktop Environment" "Select desktop environment (hover for packages):" 14 4 "${items[@]}") || true
    SELECTED_DE="${result:-NONE}"
}

# --- Category Selection ---

select_packages() {
    SELECTED_PACKAGES=()
    local items=()
    for entry in "${CATEGORY_LABELS[@]}"; do
        local key label
        key=$(echo "$entry" | cut -d'|' -f1)
        label=$(echo "$entry" | cut -d'|' -f2)
        local default="on"
        [ "$key" = "networking" ] || [ "$key" = "audio_media" ] && default="off"

        local arr_name="${CATEGORY_MAP[$key]}"
        local -n cat_array="$arr_name"
        local pkgs=()
        for pkg_entry in "${cat_array[@]}"; do
            pkgs+=("$(pkg_virtual_name "$pkg_entry")")
        done
        local IFS=','
        local help_text="Packages: ${pkgs[*]}"
        unset IFS

        items+=("$key" "$label" "$default" "$help_text")
    done

    local result
    result=$(wizard_checklist_help "Package Categories" "Select categories (hover for package list):" 20 11 "${items[@]}") || true
    local selected_categories="${result:-}"

    for entry in "${CATEGORY_LABELS[@]}"; do
        local key
        key=$(echo "$entry" | cut -d'|' -f1)
        if echo "$selected_categories" | grep -qw "$key"; then
            local arr_name="${CATEGORY_MAP[$key]}"
            local -n cat_array="$arr_name"
            local pkg_items=()
            for pkg_entry in "${cat_array[@]}"; do
                local name desc default selected
                name=$(pkg_virtual_name "$pkg_entry")
                desc=$(pkg_description "$pkg_entry")
                default=$(pkg_default "$pkg_entry")
                if [ "$default" = "1" ]; then
                    selected="on"
                else
                    selected="off"
                fi
                pkg_items+=("$name" "$desc" "$selected")
            done

            if [ ${#pkg_items[@]} -gt 0 ]; then
                local pkg_result
                pkg_result=$(wizard_checklist "$key" "Select $label packages:" 20 10 "${pkg_items[@]}") || true
                if [ -n "$pkg_result" ]; then
                    for pkg_name in $pkg_result; do
                        pkg_name=$(echo "$pkg_name" | tr -d '"')
                        SELECTED_PACKAGES+=("$pkg_name")
                    done
                fi
            fi
        fi
    done
}

# --- Resolve DE packages ---

resolve_de_packages() {
    [ "$SELECTED_DE" = "NONE" ] || [ -z "$SELECTED_DE" ] && return
    local arr_name="DE_$SELECTED_DE"
    local -n de_array="$arr_name"
    for entry in "${de_array[@]}"; do
        local name
        name=$(pkg_virtual_name "$entry")
        SELECTED_PACKAGES+=("$name")
    done
}

# --- Build install list (includes category + DE arrays) ---

build_install_list() {
    local install_list=()
    for sel_name in "${SELECTED_PACKAGES[@]}"; do
        local found=false
        for arr_name in "${CATEGORY_MAP[@]}"; do
            local -n cat_array="$arr_name"
            for pkg_entry in "${cat_array[@]}"; do
                local name
                name=$(pkg_virtual_name "$pkg_entry")
                if [ "$name" = "$sel_name" ]; then
                    install_list+=("$pkg_entry")
                    found=true
                    break 2
                fi
            done
        done
        if ! $found; then
            local de_arr="DE_$SELECTED_DE"
            if declare -p "$de_arr" &>/dev/null; then
                local -n de_array="$de_arr"
                for pkg_entry in "${de_array[@]}"; do
                    local name
                    name=$(pkg_virtual_name "$pkg_entry")
                    if [ "$name" = "$sel_name" ]; then
                        install_list+=("$pkg_entry")
                        break
                    fi
                done
            fi
        fi
    done
    echo "${install_list[@]}"
}

# --- Confirmation ---

show_confirmation() {
    local total=${#SELECTED_PACKAGES[@]}
    local de_display="$SELECTED_DE"
    [ "$OS" != "linux" ] && de_display="N/A (macOS)"

    local msg=$'Desktop Environment: '"$de_display"$'\n\n'
    msg+=$'Packages to install ('"$total"$' total):\n\n'
    for name in "${SELECTED_PACKAGES[@]}"; do
        msg+="  - $name"$'\n'
    done
    msg+=$'\nDotfiles will be deployed after installation.\n'
    msg+=$'\nProceed with installation?'

    if ! $DIALOG_CMD --title "Confirm Installation" --yesno "$msg" 25 70; then
        echo_info "Installation cancelled."
        exit 0
    fi
}

# --- Installation ---

INSTALL_LOG="$HOME/.dotfiles-install-$(date +%Y%m%d-%H%M%S).log"

run_installation() {
    local install_list=($(build_install_list))
    local total=${#install_list[@]}
    [ "$total" -eq 0 ] && echo_warn "No packages selected, skipping installation." && return

    echo_info "Installation log: $INSTALL_LOG"

    (
        local count=0 errors=0
        for entry in "${install_list[@]}"; do
            local name
            name=$(pkg_virtual_name "$entry")
            count=$((count + 1))

            if ! pkg_available "$entry"; then
                echo "[$count/$total] $name (not available on this OS)"
                continue
            fi

            {
                echo "[$count/$total] Installing $name..."
                if install_single_package "$entry" 2>&1; then
                    echo "[$count/$total] $name installed"
                else
                    echo "[$count/$total] $name failed"
                    errors=$((errors + 1))
                fi
            } | tee -a "$INSTALL_LOG"
            echo
        done

        echo "---"
        echo "$((total - errors)) packages installed"
        [ "$errors" -gt 0 ] && echo "$errors packages failed"
    ) | $DIALOG_CMD $(dialog_opts) --title "Installing Packages" --progressbox 30 85

    echo_ok "Log saved to: $INSTALL_LOG"
}

# --- Dotfile deployment ---

run_deploy() {
    echo_title "Deploying dotfiles..."
    wizard_msgbox "Dotfile Deployment" $'Dotfiles will now be deployed.\nExisting files will be backed up to:\n'"$HOME/.dotfiles-backup/"

    deploy_by_os

    echo_ok "Dotfiles deployed"
}

# --- Nvim setup ---

run_nvim_setup() {
    local has_nvim=false
    for name in "${SELECTED_PACKAGES[@]}"; do
        [ "$name" = "neovim" ] && has_nvim=true && break
    done

    if [ "$has_nvim" = true ]; then
        if wizard_yesno "Neovim" $'Install Neovim configuration from\ngermaniii/kickstart.nvim?'; then
            install_nvim_config
        fi
    fi
}

# --- Summary ---

show_summary() {
    local msg=$'Installation complete!\n\n'
    msg+="Packages installed: ${#SELECTED_PACKAGES[@]}"$'\n'
    msg+=$'Dotfiles deployed\n\n'
    msg+=$'Next steps:\n'
    msg+=$'  - Restart your terminal: source ~/.bashrc\n'
    if echo "${SELECTED_PACKAGES[@]}" | grep -qw "neovim"; then
        msg+=$'  - Open nvim and run :Mason to install LSP servers\n'
    fi
    msg+=$'  - Run tmux to start tmux\n'
    if [ "$OS" = "linux" ] && [ "$SELECTED_DE" != "NONE" ]; then
        msg+=$'  - Log out and back in to apply DE changes\n'
    fi
    msg+=$'\nBackups saved to: ~/.dotfiles-backup/'

    $DIALOG_CMD --title "Installation Complete" --msgbox "$msg" 20 70
    echo_ok "Setup complete!"
}

# --- Main ---

main() {
    welcome
    select_de
    select_packages
    resolve_de_packages
    show_confirmation
    run_installation
    run_deploy
    run_nvim_setup
    show_summary
}

main "$@"
