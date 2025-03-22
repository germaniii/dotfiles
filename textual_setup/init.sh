#!/bin/bash

echo "############################################################################"
echo "# Initial Setup"
echo "############################################################################"
rm -rf ~/.git
source ~/.bash_profile

sudo pacman-key --init
sudo pacman-key --populate
sudo pacman -Sy --noconfirm archlinux-keyring
sudo pacman -Syu --noconfirm
sudo pacman -S --noconfirm base-devel go reflector

updateMirrors
echo
echo
echo Updating Mirrors
echo
echo

echo "############################################################################"
echo "# Installing essential AUR packages"
echo "############################################################################"
AURPKGS=(
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

echo "############################################################################"
echo "# Setting up Neovim workstation"
echo "############################################################################"
rm -rf "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim
git clone -b germaniii https://github.com/germaniii/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim

echo
echo
echo "Open nvim and do :Lazy"
echo

echo "############################################################################"
echo "# Setting up development environments"
echo "############################################################################"
echo
echo "Setting up Node Version Manager"
echo
echo
source ~/.bash_profile
nvm install --lts

echo
echo "Setting up initial Miniconda environment"
echo
echo
source /opt/miniconda3/bin/activate
conda env create
conda activate dotfiles
python ./setup/main.py
