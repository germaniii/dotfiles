#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/germaniii/dotfiles.git"
REPO_BRANCH="main"
DOTFILES_DIR="$HOME/dotfiles"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[0;33m'; CYAN='\033[0;36m'; RESET='\033[0m'
echo_ok()   { echo -e "${GREEN}✓${RESET} $1"; }
echo_warn() { echo -e "${YELLOW}⚠${RESET} $1"; }
echo_err()  { echo -e "${RED}✗${RESET} $1"; }
echo_info() { echo -e "${CYAN}→${RESET} $1"; }

OS="$(uname -s)"
DISTRO=""
if [ "$OS" = "Linux" ] && [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO="$ID"
fi

if [ "$OS" = "Darwin" ] && [ -f /opt/homebrew/bin/brew ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

echo ""
echo "  ╔══════════════════════════════════════╗"
echo "  ║   Dotfiles Setup Wizard (gum)       ║"
echo "  ╚══════════════════════════════════════╝"
echo ""
echo_info "Detected OS: $OS${DISTRO:+ ($DISTRO)}"

install_brew() {
    echo_info "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    if [ -f /opt/homebrew/bin/brew ]; then
        eval "$(/opt/homebrew/bin/brew shellenv)"
    fi
    echo_ok "Homebrew installed"
}

install_gum() {
    echo_info "Installing gum (glamorous shell UI)..."
    case "$OS" in
        Darwin)
            brew install gum
            ;;
        Linux)
            case "${DISTRO:-}" in
                arch|endeavouros|manjaro|garuda)
                    sudo pacman -S --noconfirm gum
                    ;;
                *)
                    install_gum_binary
                    ;;
            esac
            ;;
    esac
}

install_gum_binary() {
    local os arch
    case "$(uname -s)" in
        Darwin) os="Darwin" ;;
        Linux)  os="Linux" ;;
        *)      echo_err "Unsupported OS"; exit 1 ;;
    esac
    case "$(uname -m)" in
        x86_64|amd64) arch="x86_64" ;;
        aarch64|arm64) arch="arm64" ;;
        *)      echo_err "Unsupported architecture"; exit 1 ;;
    esac

    local tmpdir
    tmpdir="$(mktemp -d)"
    echo_info "Downloading gum for ${os}/${arch}..."
    curl -fsSL "https://github.com/charmbracelet/gum/releases/latest/download/gum_${os}_${arch}.tar.gz" \
        | tar xz -C "$tmpdir"
    sudo mv "$tmpdir/gum" /usr/local/bin/
    rm -rf "$tmpdir"
    echo_ok "gum installed"
}

install_jq() {
    echo_info "Installing jq (JSON processor)..."
    case "$OS" in
        Darwin)
            brew install jq
            ;;
        Linux)
            case "${DISTRO:-}" in
                arch|endeavouros|manjaro|garuda)
                    sudo pacman -S --noconfirm jq
                    ;;
                ubuntu|debian|pop|elementary|linuxmint|neon)
                    sudo apt update && sudo apt install -y jq
                    ;;
                fedora)
                    sudo dnf install -y jq
                    ;;
                alpine)
                    sudo apk add jq
                    ;;
                *)
                    command -v apt && sudo apt install -y jq && return 0
                    command -v pacman && sudo pacman -S --noconfirm jq && return 0
                    command -v dnf && sudo dnf install -y jq && return 0
                    command -v apk && sudo apk add jq && return 0
                    echo_err "Could not install jq. Please install 'jq' manually."
                    exit 1
                    ;;
            esac
            ;;
    esac
}

install_yay() {
    echo_info "Installing yay (AUR helper)..."
    sudo pacman -S --noconfirm --needed base-devel git go
    local tmpdir
    tmpdir="$(mktemp -d)"
    git clone https://aur.archlinux.org/yay.git "$tmpdir/yay"
    cd "$tmpdir/yay"
    makepkg -si --noconfirm
    cd /
    rm -rf "$tmpdir"
    echo_ok "yay installed"
}

install_git() {
    echo_info "Installing git..."
    case "$OS" in
        Darwin)
            if ! command -v xcode-select &>/dev/null; then
                xcode-select --install 2>/dev/null || true
            fi
            brew install git
            ;;
        Linux)
            case "${DISTRO:-}" in
                arch|endeavouros|manjaro|garuda)
                    sudo pacman -S --noconfirm git
                    ;;
                ubuntu|debian|pop|elementary|linuxmint|neon)
                    sudo apt install -y git
                    ;;
                fedora)
                    sudo dnf install -y git
                    ;;
                alpine)
                    sudo apk add git
                    ;;
                *)
                    command -v apt && sudo apt install -y git && return 0
                    command -v pacman && sudo pacman -S --noconfirm git && return 0
                    command -v dnf && sudo dnf install -y git && return 0
                    command -v apk && sudo apk add git && return 0
                    echo_err "Could not install git. Please install 'git' manually."
                    exit 1
                    ;;
            esac
            ;;
    esac
}

if [ "$OS" = "Darwin" ] && ! command -v brew &>/dev/null; then
    install_brew
fi

if [ "$OS" = "Linux" ] && { [ "${DISTRO:-}" = "arch" ] || command -v pacman &>/dev/null; } && ! command -v yay &>/dev/null; then
    install_yay
fi

if ! command -v jq &>/dev/null; then
    install_jq
fi

if ! command -v gum &>/dev/null; then
    install_gum
fi

if ! command -v git &>/dev/null; then
    install_git
fi

echo_ok "Prerequisites installed"

if [ -d "$DOTFILES_DIR" ]; then
    echo_warn "$DOTFILES_DIR already exists."
    echo_info "Pulling latest changes..."
    cd "$DOTFILES_DIR"
    git pull origin "$REPO_BRANCH" 2>/dev/null || true
else
    echo_info "Cloning dotfiles repository..."
    git clone -b "$REPO_BRANCH" "$REPO_URL" "$DOTFILES_DIR"
fi

echo_ok "Dotfiles cloned to $DOTFILES_DIR"

echo_info "Launching interactive installer..."
cd "$DOTFILES_DIR"
exec bash "$DOTFILES_DIR/installers/gum/install.sh"
