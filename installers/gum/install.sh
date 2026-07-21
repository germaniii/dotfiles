#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "$SCRIPT_DIR/../bash/lib/detect.sh"
source "$SCRIPT_DIR/lib/wizard.sh"
source "$SCRIPT_DIR/../bash/lib/packages.sh"
source "$SCRIPT_DIR/../bash/lib/deploy.sh"
source "$SCRIPT_DIR/../bash/lib/nvim.sh"
source "$SCRIPT_DIR/../bash/lib/json_loader.sh"

if ! command -v gum &>/dev/null; then
    echo "Error: This installer requires 'gum'."
    echo "Run the setup.sh bootstrap script which installs it:"
    echo "  curl -fsSL https://raw.githubusercontent.com/germaniii/dotfiles/main/installers/gum/setup.sh | sh"
    exit 1
fi

if ! command -v jq &>/dev/null; then
    echo "Error: This installer requires 'jq' (JSON processor)."
    exit 1
fi

load_all_packages

SELECTED_PACKAGES=()
SELECTED_DE="NONE"

welcome() {
    clear
    wizard_banner "Dotfiles Setup Wizard" "" "A tool for glamorous dotfiles"

    echo
    gum style --foreground 109 "OS: $(gum style --bold "$OS")${DISTRO:+ ($(gum style --bold "$DISTRO"))}"
    gum style --foreground 109 "Package Manager: $(gum style --bold "$PKG_MANAGER")"
    echo

    if [ ! -t 0 ]; then
        echo_err "Cannot run interactively (not a terminal)"
        exit 1
    fi

    wizard_msgbox "Detected OS: $OS${DISTRO:+ ($DISTRO)} — Package Manager: $PKG_MANAGER"
}

select_de() {
    [ "$OS" != "linux" ] && return

    wizard_section "Desktop Environment Selection"

    local options=() ids=()
    for choice in "${DE_CHOICES[@]}"; do
        local name desc
        name=$(echo "$choice" | cut -d'|' -f1)
        desc=$(echo "$choice" | cut -d'|' -f2)
        options+=("$desc")
        ids+=("$name")
    done

    local result
    result=$(wizard_choose "Select desktop environment:" "${options[@]}") || true
    [ -z "$result" ] && result="Do not install a desktop environment"

    for i in "${!options[@]}"; do
        if [ "${options[$i]}" = "$result" ]; then
            SELECTED_DE="${ids[$i]}"
            break
        fi
    done
}

select_packages() {
    SELECTED_PACKAGES=()
    echo
    gum style --foreground 109 --bold "Category Selection"
    gum style --foreground 245 "Tip: use space to toggle, enter to confirm"
    echo

    local cat_options=() cat_ids=() cat_labels=()
    for entry in "${CATEGORY_LABELS[@]}"; do
        local key label
        key=$(echo "$entry" | cut -d'|' -f1)
        label=$(echo "$entry" | cut -d'|' -f2)
        cat_options+=("$label")
        cat_ids+=("$key")
        cat_labels+=("$key|$label")
    done

    local cat_result
    cat_result=$(wizard_choose_multi "Select package categories:" "${cat_options[@]}") || true

    if [ -z "$cat_result" ]; then
        echo_warn "No categories selected — nothing to install"
        return
    fi

    local selected_cats=()
    while IFS= read -r line; do
        [ -n "$line" ] && selected_cats+=("$line")
    done <<< "$cat_result"

    for cat_label in "${selected_cats[@]}"; do
        local cat_key=""
        for entry in "${CATEGORY_LABELS[@]}"; do
            local key label
            key=$(echo "$entry" | cut -d'|' -f1)
            label=$(echo "$entry" | cut -d'|' -f2)
            if [ "$label" = "$cat_label" ]; then
                cat_key="$key"
                break
            fi
        done
        [ -z "$cat_key" ] && continue

        local arr_name="${CATEGORY_MAP[$cat_key]}"
        local -n cat_array="$arr_name"
        local pkg_options=() pkg_names=()
        for pkg_entry in "${cat_array[@]}"; do
            local name desc platform_badge
            name=$(pkg_virtual_name "$pkg_entry")
            desc=$(pkg_description "$pkg_entry")
            platform_badge=$(pkg_platform_badge "$(pkg_supported_platforms "$pkg_entry")")
            [ -n "$platform_badge" ] && desc="$desc ($platform_badge)"
            pkg_options+=("$name — $desc")
            pkg_names+=("$name")
        done

        if [ ${#pkg_options[@]} -eq 0 ]; then
            continue
        fi

        local pkg_result
        pkg_result=$(wizard_choose_multi "Select $cat_label packages:" "${pkg_options[@]}") || true

        if [ -n "$pkg_result" ]; then
            while IFS= read -r pkg_line; do
                [ -n "$pkg_line" ] && SELECTED_PACKAGES+=("${pkg_line%% —*}")
            done <<< "$pkg_result"
        fi
    done
}

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

show_confirmation() {
    local total=${#SELECTED_PACKAGES[@]}
    local de_display="$SELECTED_DE"
    [ "$OS" != "linux" ] && de_display="N/A (macOS)"

    clear
    wizard_banner "Installation Summary"

    echo
    wizard_msgbox "$(gum style --bold "Desktop Environment"): $de_display" \
        "" \
        "$(gum style --bold "Packages to install"): $total"

    if [ "$total" -gt 0 ]; then
        gum style --foreground 109 --bold "Package list:"
        for name in "${SELECTED_PACKAGES[@]}"; do
            echo "  $(gum style --foreground 142 "•") $name"
        done
        echo
    fi

    gum style --foreground 245 "Dotfiles will be deployed after installation."
    echo

    if ! wizard_confirm "Proceed with installation?"; then
        echo_warn "Installation cancelled."
        exit 0
    fi
}

INSTALL_LOG="$HOME/.dotfiles-install-$(date +%Y%m%d-%H%M%S).log"

run_installation() {
    local install_list=($(build_install_list))
    local total=${#install_list[@]}
    [ "$total" -eq 0 ] && echo_warn "No packages selected, skipping installation." && return

    echo_info "Installation log: $INSTALL_LOG"
    echo

    local count=0 errors=0
    for entry in "${install_list[@]}"; do
        local name
        name=$(pkg_virtual_name "$entry")
        count=$((count + 1))

        if ! pkg_available "$entry"; then
            gum style --foreground 245 "[$count/$total] $name (not available on this OS)"
            continue
        fi

        if wizard_spinner "[$count/$total] $name" -- \
            bash -c "install_single_package \"$entry\" >> \"$INSTALL_LOG\" 2>&1"; then
            gum style --foreground 142 "[$count/$total] ✓ $name installed"
        else
            gum style --foreground 167 "[$count/$total] ✗ $name failed"
            errors=$((errors + 1))
        fi
        echo
    done

    echo "---"
    gum style --foreground 142 "$((total - errors)) packages installed"
    [ "$errors" -gt 0 ] && gum style --foreground 167 "$errors packages failed"

    echo_ok "Log saved to: $INSTALL_LOG"
}

run_deploy() {
    echo_title "Deploying dotfiles..."

    deploy_by_os

    echo_ok "Dotfiles deployed"
}

run_nvim_setup() {
    local has_nvim=false
    for name in "${SELECTED_PACKAGES[@]}"; do
        [ "$name" = "neovim" ] && has_nvim=true && break
    done

    if [ "$has_nvim" = true ]; then
        if wizard_confirm "Install Neovim configuration from germaniii/kickstart.nvim?"; then
            install_nvim_config
        fi
    fi
}

show_summary() {
    clear
    wizard_banner "Installation Complete"

    echo
    wizard_msgbox \
        "$(gum style --bold "Packages installed"): ${#SELECTED_PACKAGES[@]}" \
        "$(gum style --bold "Dotfiles"): Deployed" \
        "" \
        "$(gum style --foreground 109 "Next steps:")" \
        "  • Restart your terminal: source ~/.bashrc" \
        "  • Run tmux to start tmux" \
        "  • Log saved to: $INSTALL_LOG"

    if echo "${SELECTED_PACKAGES[@]}" | grep -qw "neovim"; then
        gum style --foreground 245 "  • Open nvim and run :Mason to install LSP servers"
    fi
    if [ "$OS" = "linux" ] && [ "$SELECTED_DE" != "NONE" ]; then
        gum style --foreground 245 "  • Log out and back in to apply DE changes"
    fi
    echo
    gum style --foreground 245 "Backups saved to: ~/.dotfiles-backup/"
    echo
    echo_ok "Setup complete!"
}

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
