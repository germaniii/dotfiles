!#/bin/bash

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

read -p "Enter the number of your choice: " choice

ARCHPKGS=(
    'ripgrep'
    'neovim'
    'cloudflared'
    'zerotier-one'
    'firewalld'
    )

if [[ $choice == 1 ]]; then
    ARCHPKGS+=('gnome')
elif [[ $choice == 2 ]]; then
    ARCHPKGS+=(
        'xfce4'
    )
elif [[ $choice == 3 ]]; then 
    ARCHPKGS+=(
        'xfce4'
        'xfce4-goodies'
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
read -p "Would you like to install terminal utilities?[Y/n]" terminal_utilities_choice

if [[ $terminal_utilities_choice == n ]]; then
    echo "Skipping Terminal Utilities Setup"
else
    echo
    echo "Installing Terminal Utilities"
    echo

    ARCHPKGS+=(
        'cronie'                  # cron jobs
        'wget'                    # Remote content retrieval
        'curl'                    # Remote content retrieval
        'bpytop'                  # Process viewer
        'neofetch'                # Shows system info when you launch terminal
        'ntp'                     # Network Time Protocol to set time via network.
        'unrar'                   # RAR compression program
        'unzip'                   # Zip compression program
        'zip'                     # Zip compression program
        'ranger'    	      # Filesystem browser
        'bpytop'
        'pipewire'
        'wireplumber'
        'networkmanager'
        'ack'
        'nodejs'
        'fzf'
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
read -p "Would you like to install aur pakages?[Y/n]" aur_packs_choice

AURPKGS=(
    # UTILITIES -----------------------------------------------------------
    'timeshift'                 # Backup and Restore
    'rofi-lbonn-wayland-git'
    # 'zerotier-one'
    'docker'
    'docker-compose'
    'gruvbox-material-icon-theme-git'
    'gruvbox-material-gtk-theme-git'
    'ttf-fira-code'
    'ttf-font-awesome'
    'wlrobs-hg'
    'tlpui'
)

cd ${HOME}/yay
makepkg -si

for PKG in "${AURPKGS[@]}"; do
    yay -S --noconfirm $PKG
done

echo
echo "Done!"
echo

# NVIM Install kickstart.nvim
git clone -b germaniii https://github.com/germaniii/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim

############################################################################
# NVIM SETUP
############################################################################

echo
echo "Setting up Neovim workstation"
echo

# Install COC Node.js for lsp
echo 
echo "Open nvim and do :Lazy"
echo

# Setup crontab
crontab < /home/germaniii/.crontab