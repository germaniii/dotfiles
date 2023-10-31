#!/bin/sh
picom & 
feh --randomize --bg-fill /usr/share/backgrounds/* &
blueman-applet &
nm-applet &
kitty -e bpytop &
sleep .5 &
kitty -e bash -c 'neofetch && bash' --hold &
sleep .5 &
flameshot &
copyq &
