# Dotfiles

Cross-platform dotfiles for macOS (AeroSpace) and Linux (Hyprland).

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/germaniii/dotfiles/main/installers/bash/setup.sh | sh
```

The installer auto-detects your OS and package manager, then guides you through:

- **Desktop Environment** selection (Linux: GNOME/XFCE/Hyprland)
- **Package selection** by category (Terminal Utilities, Development, Fonts, etc.)
- **Dotfile deployment** with automatic backup of existing configs
- **Neovim setup** from [germaniii/kickstart.nvim](https://github.com/germaniii/kickstart.nvim)

## Supported Platforms

| OS | Package Manager | Status |
|---|---|---|
| macOS | Homebrew | ✓ |
| Arch Linux | pacman + yay (AUR) | ✓ |
| Debian/Ubuntu | apt | ✓ |

## Package Categories

- **Desktop Environment** - GNOME, XFCE, Hyprland (Linux only)
- **Terminal Utilities** - fzf, ripgrep, fd, htop, tmux, ranger, neovim, starship
- **Terminal Emulators** - kitty, ghostty
- **Development - Core** - git, docker, build tools
- **Development - Runtimes** - Go, Ruby, Rust, Java, Node, Python, Julia, Zig, etc.
- **Development - LSP Tools** - terraform, sqlfluff, buf, shellcheck, prettier, etc.
- **Fonts** - Fira Code, Noto, DejaVu, Nerd Fonts
- **Theming** - Gruvbox GTK theme, Rofi themes, SDDM themes
- **Applications** - GIMP, OBS, Flameshot, CopyQ, Timeshift
- **Audio & Media** - PipeWire, FFmpeg, ImageMagick
- **Networking** - NetworkManager, Cloudflare Tunnel, firewall
- **System Utilities** - cron, unzip, direnv, LaTeX engine

## Installers

```
installers/
  bash/             # Bash/dialog interactive wizard
  # (future: nix/, docker/, etc.)
```

## Directory Structure

```
dotfiles/
  installers/
    bash/           # Installer scripts
      setup.sh      # Bootstrap: curl | sh entry point
      install.sh    # Interactive dialog/whiptail wizard
      lib/          # Library scripts
      packages/     # Package definitions by platform
  configs/
    common/         # Cross-platform dotfiles (.bashrc, starship, tmux, etc.)
    linux/          # Linux-specific (hyprland, waybar, kitty, rofi, etc.)
    macos/          # macOS-specific (aerospace, ghostty)
  themes/           # Gruvbox GTK theme
```

## Manual Install

```bash
git clone -b main https://github.com/germaniii/dotfiles ~/dotfiles
cd ~/dotfiles
./installers/bash/install.sh
```
