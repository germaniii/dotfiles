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

# --- Ensure brew is in PATH (Apple Silicon) ---
if [ "$OS" = "Darwin" ] && [ -f /opt/homebrew/bin/brew ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

echo ""
echo "  ╔══════════════════════════════════════╗"
echo "  ║      Dotfiles Setup Wizard           ║"
echo "  ╚══════════════════════════════════════╝"
echo ""
echo_info "Detected OS: $OS${DISTRO:+ ($DISTRO)}"

# --- Install Homebrew (macOS only) ---

install_brew() {
    echo_info "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    if [ -f /opt/homebrew/bin/brew ]; then
        eval "$(/opt/homebrew/bin/brew shellenv)"
    fi
    echo_ok "Homebrew installed"
}

# --- Install dialog ---

install_dialog() {
    echo_info "Installing dialog (interactive menus)..."
    case "$OS" in
        Darwin)
            brew install dialog
            ;;
        Linux)
            case "$DISTRO" in
                arch|endeavouros|manjaro|garuda)
                    sudo pacman -S --noconfirm dialog
                    ;;
                ubuntu|debian|pop|elementary|linuxmint|neon)
                    sudo apt update && sudo apt install -y dialog
                    ;;
                fedora)
                    sudo dnf install -y dialog
                    ;;
                alpine)
                    sudo apk add dialog
                    ;;
                *)
                    command -v apt && sudo apt install -y dialog && return 0
                    command -v pacman && sudo pacman -S --noconfirm dialog && return 0
                    command -v dnf && sudo dnf install -y dialog && return 0
                    command -v apk && sudo apk add dialog && return 0
                    echo_err "Could not install dialog. Please install 'dialog' manually."
                    exit 1
                    ;;
            esac
            ;;
    esac
}

# --- Install yay (Arch Linux AUR helper) ---

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

# --- Install git ---

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
            case "$DISTRO" in
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

# --- Install prerequisites ---

if [ "$OS" = "Darwin" ] && ! command -v brew &>/dev/null; then
    install_brew
fi

if [ "$OS" = "Linux" ] && { [ "$DISTRO" = "arch" ] || command -v pacman &>/dev/null; } && ! command -v yay &>/dev/null; then
    install_yay
fi

if ! command -v dialog &>/dev/null && ! command -v whiptail &>/dev/null; then
    install_dialog
fi

if ! command -v git &>/dev/null; then
    install_git
fi

echo_ok "Prerequisites installed"

# --- Clone repo ---

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
exec bash "$DOTFILES_DIR/installers/bash/install.sh"
