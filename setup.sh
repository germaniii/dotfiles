#!/bin/bash

############################################################################
# DE SELECTION
############################################################################

# Provide a menu for the user to select the desktop environment
echo "Select your desktop environment:"
echo "1. GNOME"
echo "2. Xfce desktop only"
echo "3. Xfce with Goodies"
echo "4. Hyprland"
echo "5. Skip"
echo "6. Quit"

read -rp "Enter the number of your choice: " choice

ARCHPKGS=()

if [[ $choice == 1 ]]; then
    ARCHPKGS+=('gnome')
elif [[ $choice == 2 ]]; then
    ARCHPKGS+=(
        'xfce4'
        'x11vnc'
    )
elif [[ $choice == 3 ]]; then 
    ARCHPKGS+=(
        'xfce4'
        'xfce4-goodies'
        'x11vnc'
    )
elif [[ $choice == 4 ]]; then
    ARCHPKGS+=(
        'hyprland'
        'hyprpaper'
        'hyprlock'
        'xdg-desktop-portal-hyprland'
        'wlogout'
        'waybar'
        'kitty'
        'grim'
        'slurp'
        'dunst'
        'polkit-kde-agent'
        'swaylock'
        'swayidle'
        'gdm'
        'brightnessctl'
        'acpi'
        'poweralertd'
        'blueman'
        'copyq'
        'wl-clipboard'
        'sddm'
    )
elif [[ $choice == 5 ]]; then
    echo "Skipped Installing Desktop Environment"
else
    echo "Invalid choice. Please enter a valid number."
    exit 1
fi

############################################################################
# ARCH TERMINAL UTILITIES
############################################################################
read -rp "[Terminal] Would you like to install essential utilities?[Y/n]" terminal_utilities_choice

if [[ $terminal_utilities_choice != n ]]; then
    echo
    echo "Installing Terminal Utilities"
    echo

    ARCHPKGS+=(
        # Workflow Essentials
        'fzf'
        'ripgrep'
        'sed'
        'neovim'
        'tmux'
        'ack'
        'ranger'
        'htop'
        'fastfetch'
        'entr' # tmux dep

        # Networking Essentials
        'wget'                    # Remote content retrieval
        'curl'                    # Remote content retrieval
        'ntp'                     # Network Time Protocol to set time via network.
        'networkmanager'
        'cloudflared'
        'firewalld'
        'reflector'

        # Programming essentials
        'base-devel'
        'git'
        'docker'
        'docker-compose'

        # Audio Essentials
        'pipewire'
        'wireplumber'

        # Additional but not Optional
        'cronie'                  # cron jobs
        'unrar'                   # RAR compression program
        'unzip'                   # Zip compression program
        'zip'                     # Zip compression program
    )

    for PKG in "${ARCHPKGS[@]}"; do
        echo "INSTALLING: ${PKG}"
        sudo pacman -S "$PKG" --noconfirm --needed
    done

    # Update font cache
    sudo fc-cache --force

    echo
    echo "Done!"
    echo
fi

############################################################################
# AUR TERMINAL UTILITIES
############################################################################
read -rp "[Terminal] Would you like to install essential aur pakages?[Y/n]" aur_packs_choice

if [[ $aur_packs_choice != n ]]; then
    AURPKGS=(
        'tmux-plugin-manager'
        'ttf-fira-code'
        'ttf-font-awesome'
    )
fi

read -rp "[Terminal & GUI] Would you like to install additional fonts?[Y/n]" additional_fonts_choice

if [[ $additional_fonts_choice != n ]]; then
    AURPKGS+=(
        'ttf-freefont'
        'ttf-ms-fonts'
        'ttf-linux-libertine'
        'ttf-dejavu'
        'ttf-inconsolata'
        'ttf-ubuntu-font-family'
        'noto-fonts-cjk'
        'noto-fonts-emoji'
        'noto-fonts'
    )
fi

read -rp "[GUI] Would you like to install additional theming for TWMs? [Y/n]" additional_twm_theming_choice

if [[ $additional_twm_theming_choice != n ]]; then
    AURPKGS+=(
        'rofi-lbonn-wayland-git'
        'gruvbox-material-icon-theme-git'
        'gruvbox-material-gtk-theme-git'
        'sddm-sugar-dark'
    )
fi


read -rp "[GUI] Would you like to install additional apps for Desktop?[Y/n]" additional_apps_choice

if [[ $additional_apps_choice != n ]]; then
    AURPKGS+=(
        'obs-studio'
        'wlrobs-hg'                 # Used in OBS Studio and Screen Sharing
        'timeshift'                 # Backup and Restore
    )
fi

# Install yay
cd ~ || exit
git clone https://aur.archlinux.org/yay.git
cd yay || exit
makepkg -si
cd ~ || exit
rm -rf ~/yay

for PKG in "${AURPKGS[@]}"; do
    yay -S --noconfirm "$PKG"
done

echo
echo "Done!"
echo

############################################################################
# NVIM SETUP
############################################################################

echo
echo "Setting up Neovim workstation"
echo

# NVIM Install kickstart.nvim
git clone -b germaniii https://github.com/germaniii/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim

# Install COC Node.js for lsp
echo 
echo "Open nvim and do :Lazy"
echo

# Setup crontab
if [ -f ~/.crontab ]; then
    crontab < ~/.crontab
fi
