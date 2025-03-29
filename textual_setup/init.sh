#!/bin/bash

echo "############################################################################"
echo "# Initial Setup"
echo "############################################################################"
rm -rf ~/.git
source ~/.bash_profile

sudo pacman-key --init
sudo pacman-key --populate
sudo pacman -Sy --noconfirm archlinux-keyring
sudo pacman -S --noconfirm reflector

echo "############################################################################"
echo "# Updating Mirrors"
echo "############################################################################"
source ~/.bash_aliases
updateMirrors

echo "############################################################################"
echo "# Updating System"
echo "############################################################################"
sudo pacman -Syu --noconfirm

echo "############################################################################"
echo "# Installing Essential Packages"
echo "############################################################################"
sudo pacman -S --noconfirm base-devel go mise

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
source ~/.bash_profile
eval "$(mise activate bash)"
mise trust
mise install

echo "############################################################################"
echo "# Installing Essential Python Packages"
echo "############################################################################"
pip install -r ./requirements.txt
python ./setup/main.py
