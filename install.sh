# Install Brew package manager
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install bash

# Set Bash default shell
echo "/opt/homebrew/bin/bash" >> /etc/shells 
chsh -s /opt/homebrew/bin/bash

brew install starship \
	fastfetch \
	ghostty \
	zen \ #firefox-based
	arc \ #chromium-based
	wget \
	git \
	coreutils \
	gh \
	ffmpeg \
	# neovim tings
	neovim \
	fzf \
	ripgrep \
	fd \
	imagemagick \
	gs \
	tectonic \
	# tmux tings
	tpm \
	tmux

brew install --cask font-fira-code
brew install --cask nikitabobko/tap/aerospace
brew install --cask mediosz/tap/swipeaerospace
brew install --cask --no-quarantine middleclick
brew install --cask gimp
# macos notch 
# brew install --cask TheBoredTeam/boring-notch/boring-notch --no-quarantine
# Battery Toolkit
brew tap mhaeuser/mhaeuser
brew install battery-toolkit --no-quarantine

# install mise
curl https://mise.run | sh

#install neovim config
git clone https://github.com/germaniii/kickstart.nvim/tree/germaniii ~/.config/nvim

# copy configuration
cp -r .config ~
cp -r .tmux.conf ~
