#!/bin/bash

############################################################################
# Initial Setup
############################################################################
rm -rf ~/.git
source ~/.bash_profile

sudo pacman-key --init
sudo pacman-key --populate
sudo pacman -Sy archlinux-keyring
sudo pacman -Syu
sudo pacman -S --noconfirm base-devel go reflector

echo
echo Updating Mirrors
echo
updateMirrors

############################################################################
# AUR TERMINAL UTILITIES
############################################################################
AURPKGS=(
    'neovim'
    'nvm'
    'miniconda3'
)

# Install yay
git clone https://aur.archlinux.org/yay.git
cd yay || exit
makepkg -si
cd .. || exit
rm -rf yay

for PKG in "${AURPKGS[@]}"; do
    yay -S --noconfirm "$PKG"
done

# Setup crontab
# if [ -f ~/.crontab ]; then
#     crontab < ~/.crontab
# fi

############################################################################
# NeoVim SETUP
############################################################################

echo
echo "Setting up Neovim workstation"
echo

# NeoVim Install kickstart.nvim
git clone -b germaniii https://github.com/germaniii/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim

# Install Node.js for lsp
echo 
echo "Open nvim and do :Lazy"
echo

############################################################################
# Development Environments SETUP
############################################################################

echo
echo "Setting up Environments"
echo

echo
echo "Setting up Node Version Manager"
echo
source ~/.bash_profile
nvm install --lts

echo
echo "Setting up initial Miniconda environment"
echo
source /opt/miniconda3/bin/activate
conda env create -f ./dotfiles.yml
conda activate dotfiles
python -m setup.main
