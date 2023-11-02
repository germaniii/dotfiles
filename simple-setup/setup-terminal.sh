!#/bin/bash

############################################################################
# DE SELECTION
############################################################################

# Provide a menu for the user to select the desktop environment
echo "Select your desktop environment:"
echo "1. GNOME"
echo "2. Qtile"
echo "3. Xfce desktop only"
echo "4. Xfce with Goodies"
echo "5. Hyprland"
echo "6. Skip"
echo "7. Quit"

read -p "Enter the number of your choice: " choice

ARCHPKGS=()

if [[ $choice == 1 ]]; then
    ARCHPKGS+=('gnome')
elif [[ $choice == 2 ]]; then
    ARCHPKGS+=(
        'qtile'
        'rofi'
        'flameshot'
        'kitty'
        'feh'
        'dunst'
        'copyq'
        'picom'
        'ufw'
        'lightdm'
        'arandr'
        'pipewire'
        'lib32-pipewire'
        'helvum'
    )
elif [[ $choice == 3 ]]; then
    ARCHPKGS+=(
        'xfce4'
        'ufw'
    )
elif [[ $choice == 4 ]]; then 
    ARCHPKGS+=(
        'xfce4'
        'xfce4-goodies'
    )
elif [[ $choice == 5 ]]; then
    ARCHPKGS+=(
        'hyprland'
        'hyprpaper'
        'waybar'
        'wofi'
        'kitty'
        'networkmanager'
        'grim'
        'slurp'
    )
elif [[ $choice == 6 ]]; then
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
        'curl'                    # Remote content retrieval
        'gtop'                    # System monitoring via terminal
        'gufw'                    # Firewall manager
        'hardinfo'                # Hardware info app
        'bpytop'                  # Process viewer
        'neofetch'                # Shows system info when you launch terminal
        'ntp'                     # Network Time Protocol to set time via network.
        'unrar'                   # RAR compression program
        'unzip'                   # Zip compression program
        'wget'                    # Remote content retrieval
        'vim'                     # Terminal Editor
        'zip'                     # Zip compression program
        'ranger'    	      # Filesystem browser
        'feh'  	              # Wallpaper changer
        'neovim'
        'bpytop'
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
    # 'zerotier-one'
    'docker'
    'docker-compose'
    'gruvbox-material-icon-theme-git'
    'gruvbox-material-gtk-theme-git'
    'ttf-fira-code'
    'ttf-font-awesome'
)

cd ${HOME}/yay
makepkg -si

for PKG in "${AURPKGS[@]}"; do
    yay -S --noconfirm $PKG
done

echo
echo "Done!"
echo

# NVIM Install with vim-plug
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

############################################################################
# NVIM SETUP
############################################################################

echo
echo "Setting up Neovim workstation"
echo

# Install COC Node.js for lsp

# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
nvm_setup_code='
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
'
# Append the code to .bashrc if it doesn't already exist
if ! grep -q "This loads nvm" ~/.bashrc; then
    echo "$nvm_setup_code" >> ~/.bashrc
    echo "NVM setup code added to ~/.bashrc"
else
    echo "NVM setup code is already in ~/.bashrc"
fi

echo
echo "Please install nvm lts if node fails in neovim"
echo "Then open nvim and do :PlugInstall"
echo

source ~/.bashrc
nvm install --lts


