#!/bin/bash

############################################################################
# Initial Setup
############################################################################
sudo pacman -Syu
sudo pacman -S --noconfirm base-devel

############################################################################
# AUR TERMINAL UTILITIES
############################################################################
AURPKGS=(
    'neovim'
    'nvm'
    'miniconda'
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
if [ -f ~/.crontab ]; then
    crontab < ~/.crontab
fi

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
nvm install --lts

echo
echo "Setting up initial Miniconda environment"
echo
conda env create -f ./dotfiles-installer.yml
conda activate dotfiles-installer
python py-install.py
