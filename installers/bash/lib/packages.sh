get_platform_pkg_name() {
    local entry="$1" field="$2"
    echo "$entry" | cut -d'|' -f"$field"
}

pkg_virtual_name()   { get_platform_pkg_name "$1" 1; }
pkg_method()         { get_platform_pkg_name "$1" 2; }
pkg_arch()           { get_platform_pkg_name "$1" 3; }
pkg_debian()         { get_platform_pkg_name "$1" 4; }
pkg_macos()          { get_platform_pkg_name "$1" 5; }
pkg_default()        { get_platform_pkg_name "$1" 6; }
pkg_description()    { get_platform_pkg_name "$1" 7; }

resolve_pkg_name() {
    local entry="$1"
    local method arch debian macos
    method=$(pkg_method "$entry")
    arch=$(pkg_arch "$entry")
    debian=$(pkg_debian "$entry")
    macos=$(pkg_macos "$entry")
    case "$OS" in
        macos) echo "$macos" ;;
        linux)
            case "$DISTRO" in
                arch)   echo "$arch" ;;
                debian) echo "$debian" ;;
                fedora) echo "$arch" ;;
                alpine) echo "$arch" ;;
                *)      echo "$arch" ;;
            esac
            ;;
        *) echo "" ;;
    esac
}

pkg_available() {
    local name
    name=$(resolve_pkg_name "$1")
    [ -n "$name" ] && [ "$name" != "-" ]
}

install_single_package() {
    local entry="$1"
    local name method
    name=$(pkg_virtual_name "$entry")
    method=$(pkg_method "$entry")

    if ! pkg_available "$entry"; then
        echo "skip"
        return 0
    fi

    local pkg_name
    pkg_name=$(resolve_pkg_name "$entry")

    case "$method" in
        pkg)
            local cmd
            cmd=$(pkg_install_cmd "$PKG_MANAGER")
            if [ "$cmd" = "unknown" ]; then
                echo_err "No package manager for $OS/$DISTRO"
                return 1
            fi
            eval "$cmd $pkg_name"
            ;;
        aur)
            if [ "$DISTRO" != "arch" ]; then
                echo_err "AUR packages only available on Arch Linux"
                return 1
            fi
            if ! has_yay; then
                echo_err "AUR package requires yay (install yay first)"
                return 1
            fi
            yay -S --noconfirm "$pkg_name"
            ;;
        go)
            command -v go &>/dev/null || { echo_err "go not installed"; return 1; }
            go install "${pkg_name}@latest"
            ;;
        cargo)
            command -v cargo &>/dev/null || { echo_err "cargo not installed"; return 1; }
            cargo install "$pkg_name"
            ;;
        pip)
            command -v pip3 &>/dev/null || command -v pip &>/dev/null || { echo_err "pip not installed"; return 1; }
            local pip_cmd
            pip_cmd=$(command -v pip3 || command -v pip)
            $pip_cmd install "$pkg_name"
            ;;
        gem)
            command -v gem &>/dev/null || { echo_err "gem (Ruby) not installed"; return 1; }
            gem install "$pkg_name"
            ;;
        npm)
            command -v npm &>/dev/null || { echo_err "npm not installed"; return 1; }
            npm install -g "$pkg_name"
            ;;
        custom)
            if declare -f "install_custom_${name}" &>/dev/null; then
                "install_custom_${name}"
            else
                echo_err "No custom installer for $name"
                return 1
            fi
            ;;
        *)
            echo_err "Unknown install method: $method"
            return 1
            ;;
    esac
}

filter_selected_packages() {
    local category_name="$1" selected_list="$2"
    local -n category_ref="$category_name"
    local result=()
    for entry in "${category_ref[@]}"; do
        local name
        name=$(pkg_virtual_name "$entry")
        if echo "$selected_list" | grep -qw "$name"; then
            result+=("$entry")
        fi
    done
    echo "${result[@]}"
}

get_default_packages() {
    local category_name="$1"
    local -n category_ref="$category_name"
    local result=()
    for entry in "${category_ref[@]}"; do
        local default
        default=$(pkg_default "$entry")
        if [ "$default" = "1" ]; then
            local name
            name=$(pkg_virtual_name "$entry")
            result+=("$name")
        fi
    done
    echo "${result[@]}"
}

get_all_package_names() {
    local category_name="$1"
    local -n category_ref="$category_name"
    local names=()
    for entry in "${category_ref[@]}"; do
        local name
        name=$(pkg_virtual_name "$entry")
        names+=("$name")
    done
    echo "${names[@]}"
}

build_wizard_items() {
    local category_name="$1" selected_list="$2"
    local -n category_ref="$category_name"
    local items=()
    for entry in "${category_ref[@]}"; do
        local name desc default
        name=$(pkg_virtual_name "$entry")
        desc=$(pkg_description "$entry")
        local selected="off"
        if echo "$selected_list" | grep -qw "$name"; then
            selected="on"
        fi
        items+=("$name" "$desc" "$selected")
    done
    echo "${items[@]}"
}
