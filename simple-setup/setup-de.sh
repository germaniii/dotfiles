############################################################################
# ARCH TERMINAL UTILITIES
############################################################################


ARCHPKGS=(
    'picom'
    'gruvbox-material-icon-theme-git'
    'gruvbox-material-gtk-theme-git'
    'qtile'
    'dunst'
    'rofi'
    'flameshot'
    'kitty'
    'feh'
    'ranger'
    'handbrake'	      # Video codec converter
    'ffmpeg'	      # audio and video codecs
    'vlc'             # Video player
    'gimp'	      # Photo Editor
    'copyq'
    'git'                   # Version control system
    'ttf-fira-code'
    'tmux'
    'bpytop'
    'network-manager-applet'
    'arandr'
)

for PKG in "${ARCHPKGS[@]}"; do
    yay -S --noconfirm $PKG
done

echo
echo "Done!"
echo

#Backgrounds
echo Downloading Backgrounds
git clone https://github.com/germaniii/arch-backgrounds
sudo mkdir -p /usr/share/backgrounds/
sudo cp -r ~/arch-backgrounds/* /usr/share/backgrounds/
sudo rm -rf /usr/share/backgrounds/gnome
sudo rm -rf ~/arch-backgrounds
