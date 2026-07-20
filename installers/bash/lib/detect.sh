detect_os() {
    case "$(uname -s)" in
        Darwin) echo "macos" ;;
        Linux)  echo "linux" ;;
        *)      echo "unknown" ;;
    esac
}

detect_linux_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        case "$ID" in
            arch|endeavouros|manjaro|garuda) echo "arch" ;;
            ubuntu|debian|pop|elementary|linuxmint|neon) echo "debian" ;;
            fedora) echo "fedora" ;;
            alpine) echo "alpine" ;;
            *) echo "$ID" ;;
        esac
    elif command -v pacman &>/dev/null; then
        echo "arch"
    elif command -v apt &>/dev/null; then
        echo "debian"
    else
        echo "unknown"
    fi
}

detect_package_manager() {
    local os="$1" distro="$2"
    case "$os" in
        macos)
            if command -v brew &>/dev/null; then
                echo "brew"
            else
                echo "none"
            fi
            ;;
        linux)
            case "$distro" in
                arch)   echo "pacman" ;;
                debian) echo "apt" ;;
                fedora) echo "dnf" ;;
                alpine) echo "apk" ;;
                *)      echo "unknown" ;;
            esac
            ;;
        *) echo "unknown" ;;
    esac
}

pkg_install_cmd() {
    local pm="$1"
    case "$pm" in
        brew)   echo "brew install" ;;
        pacman) echo "sudo pacman -S --noconfirm" ;;
        apt)    echo "sudo apt install -y" ;;
        dnf)    echo "sudo dnf install -y" ;;
        apk)    echo "sudo apk add" ;;
        *)      echo "unknown" ;;
    esac
}

pkg_update_cmd() {
    local pm="$1"
    case "$pm" in
        brew)   echo "brew update" ;;
        pacman) echo "sudo pacman -Syu --noconfirm" ;;
        apt)    echo "sudo apt update" ;;
        dnf)    echo "sudo dnf check-update" ;;
        apk)    echo "sudo apk update" ;;
        *)      echo "unknown" ;;
    esac
}

has_yay() {
    command -v yay &>/dev/null
}

has_dialog() {
    command -v dialog &>/dev/null || command -v whiptail &>/dev/null
}

detect_shell() {
    basename "${SHELL:-bash}"
}

get_dialog_cmd() {
    if command -v dialog &>/dev/null; then
        echo "dialog"
    else
        echo "whiptail"
    fi
}

OS=$(detect_os)
DISTRO=$(detect_linux_distro)
PKG_MANAGER=$(detect_package_manager "$OS" "$DISTRO")
HAS_YAY=$(has_yay && echo true || echo false)
DIALOG_CMD=$(get_dialog_cmd)
