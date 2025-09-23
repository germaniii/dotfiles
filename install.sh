# Set Bash default shell
echo "/opt/homebrew/bin/bash" >> /etc/shells 
chsh -s /opt/homebrew/bin/bash

# Install Brew package manager
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install starship \
	neovim \
	fastfetch \
	ghostty \
	tpm \
	tmux

brew install --cask nikitabobko/tap/aerospace

# install mise
curl https://mise.run | sh

#install neovim config
git clone https://github.com/germaniii/kickstart.nvim/tree/germaniii ~/.config/nvim

# copy configuration
cp -r .config ~
cp -r .tmux.conf ~
