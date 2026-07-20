# Package definitions
# Format: "virtual_name|method|arch|debian|macos|default|description"
# method: pkg, aur, go, cargo, pip, npm, custom
# default: 1 = selected by default in wizard, 0 = opt-in
# "-" = not available on that platform

# --- Desktop Environment bundles (special - selected via radiolist) ---
# Each DE defines a list of packages; selecting the DE adds all of them

readonly DE_GNOME=(
    "gnome|pkg|gnome|gnome|-|0|Complete GNOME desktop environment"
)

readonly DE_XFCE=(
    "xfce4|pkg|xfce4|xfce4|-|0|Lightweight GTK desktop environment"
    "xfce4-goodies|pkg|xfce4-goodies|xfce4-goodies|-|0|Xfce extras and plugins"
    "x11vnc|pkg|x11vnc|x11vnc|-|0|VNC server for remote access"
)

readonly DE_HYPRLAND=(
    "hyprland|pkg|hyprland|hyprland|-|0|Dynamic Wayland tiling compositor"
    "hyprpaper|pkg|hyprpaper|-|-|0|Wallpaper utility for Hyprland"
    "hyprlock|pkg|hyprlock|-|-|0|GPU-accelerated screen locker"
    "xdg-desktop-portal-hyprland|pkg|xdg-desktop-portal-hyprland|-|-|0|XDG desktop portal for Hyprland"
    "waybar|pkg|waybar|waybar|-|0|GTK status bar for wlroots compositors"
    "wlogout|pkg|wlogout|-|-|0|Logout menu for Wayland"
    "grim|pkg|grim|grim|-|0|Wayland screenshot utility"
    "slurp|pkg|slurp|slurp|-|0|Wayland region selector"
    "dunst|pkg|dunst|dunst|-|0|Lightweight notification daemon"
    "polkit-kde-agent|pkg|polkit-kde-agent|-|-|0|KDE Polkit authentication agent"
    "swaylock|pkg|swaylock|swaylock|-|0|Wayland screen locker"
    "swayidle|pkg|swayidle|swayidle|-|0|Wayland idle management daemon"
    "brightnessctl|pkg|brightnessctl|-|-|0|Screen brightness control"
    "acpi|pkg|acpi|acpi|-|0|Battery and power info"
    "blueman|pkg|blueman|blueman|-|0|Bluetooth manager"
    "wl-clipboard|pkg|wl-clipboard|wl-clipboard|-|0|Wayland clipboard utilities"
)

# --- Terminal Utilities ---

readonly TERMINAL_UTILITIES=(
    "fzf|pkg|fzf|fzf|fzf|1|Command-line fuzzy finder"
    "ripgrep|pkg|ripgrep|ripgrep|ripgrep|1|Fast recursive text search"
    "fd|pkg|fd|fd-find|fd|1|Fast alternative to find"
    "htop|pkg|htop|htop|htop|1|Interactive process viewer"
    "fastfetch|pkg|fastfetch|fastfetch|fastfetch|1|System information tool"
    "tmux|pkg|tmux|tmux|tmux|1|Terminal multiplexer"
    "ranger|pkg|ranger|ranger|ranger|1|Terminal file manager"
    "wget|pkg|wget|wget|wget|1|File retriever for web"
    "curl|pkg|curl|curl|curl|1|Data transfer utility"
    "neovim|pkg|neovim|neovim|neovim|1|Modern Vim-based editor"
    "starship|pkg|starship|starship|starship|1|Cross-shell prompt"
    "entr|pkg|entr|entr|entr|1|File change trigger"
)

# --- Terminal Emulators ---

readonly TERMINAL_EMULATORS=(
    "kitty|pkg|kitty|kitty|kitty|0|Fast GPU-accelerated terminal"
    "ghostty|pkg|ghostty|ghostty|ghostty|1|Native GPU-accelerated terminal"
)

# --- Development: Core (always recommended) ---

readonly DEV_CORE=(
    "git|pkg|git|git|git|1|Distributed version control"
    "docker|pkg|docker|docker.io|docker|1|Containerization platform"
    "docker-compose|pkg|docker-compose|docker-compose-v2|-|1|Multi-container Docker apps"
    "mise|pkg|mise|mise|mise|0|Multi-language version manager"
    "base-devel|pkg|base-devel|build-essential|-|1|Essential build tools"
    "go|pkg|go|golang|go|0|Go programming language"
)

# --- Development: Runtimes ---

readonly DEV_RUNTIMES=(
    "go|pkg|go|golang|go|0|Go programming language"
    "ruby|pkg|ruby|ruby|ruby|0|Ruby programming language"
    "rust|pkg|rust|rustc|rustup|0|Rust systems programming language"
    "java-jdk|pkg|jdk-openjdk|default-jdk|openjdk|0|Java Development Kit"
    "nodejs|pkg|nodejs|nodejs|node|0|JavaScript runtime"
    "python|pkg|python|python3|python3|1|Python programming language"
    "julia|pkg|julia|-|julia|0|Julia scientific computing language"
    "zig|pkg|zig|-|zig|0|Zig systems programming language"
    "nim|pkg|nim|-|nim|0|Nim programming language"
    "elm|pkg|elm|-|elm|0|Elm functional language"
    "clojure|pkg|clojure|-|clojure|0|Clojure Lisp dialect"
    "dart|pkg|dart|dart|dart|0|Dart programming language"
    "elixir|pkg|elixir|elixir|elixir|0|Elixir language (Erlang VM)"
)

# --- Development: LSP Tools & Formatters ---

readonly DEV_LSP_TOOLS=(
    "gopls|pkg|gopls|gopls|-|0|Go language server"
    "rust-analyzer|pkg|rust-analyzer|-|-|0|Rust language server"
    "terraform|pkg|terraform|terraform|terraform|0|Infrastructure as code (Terraform)"
    "tflint|pkg|tflint|tflint|tflint|0|Terraform linter"
    "buf|go|github.com/bufbuild/buf/cmd/buf|-|-|0|Protobuf tooling"
    "sqlfluff|pip|sqlfluff|sqlfluff|sqlfluff|0|SQL linter and formatter"
    "yamlfmt|go|github.com/google/yamlfmt/cmd/yamlfmt|-|-|0|YAML formatter"
    "golangci-lint|go|github.com/golangci/golangci-lint/cmd/golangci-lint|-|-|0|Go linter"
    "shellcheck|pkg|shellcheck|shellcheck|shellcheck|0|Shell script linter"
    "hadolint|pkg|hadolint|hadolint|hadolint|0|Dockerfile linter"
    "markdownlint|npm|markdownlint-cli|-|-|0|Markdown linter"
    "stylua|pkg|stylua|stylua|stylua|0|Lua formatter"
    "prettier|npm|prettier|-|-|0|Multi-language code formatter"
    "shfmt|pkg|shfmt|shfmt|shfmt|0|Shell script formatter"
)

# --- Fonts ---

readonly FONTS=(
    "nerd-fonts-symbols|pkg|ttf-nerd-fonts-symbols|-|font-nerd-fonts-symbols|1|Nerd Fonts symbols"
    "noto-fonts|pkg|noto-fonts|fonts-noto|font-noto|1|Noto font family"
    "noto-fonts-cjk|pkg|noto-fonts-cjk|fonts-noto-cjk|font-noto-sans-cjk|1|CJK font support"
    "noto-fonts-emoji|pkg|noto-fonts-emoji|fonts-noto-color-emoji|font-noto-emoji|1|Emoji font support"
    "dejavu-fonts|pkg|ttf-dejavu|fonts-dejavu-core|font-dejavu|1|DejaVu font family"
    "ubuntu-font|pkg|ttf-ubuntu-font-family|fonts-ubuntu|font-ubuntu|1|Ubuntu font family"
    "inconsolata|pkg|ttf-inconsolata|fonts-inconsolata|font-inconsolata|1|Monospace font"
    "libertine-fonts|pkg|ttf-linux-libertine|fonts-linuxlibertine|font-libertine-mono|0|Linux Libertine fonts"
    "ms-fonts|aur|ttf-ms-fonts|-|-|0|Microsoft TrueType core fonts"
    "fira-code|pkg|ttf-fira-code|fonts-firacode|font-fira-code|1|Fira Code monospace font"
)

# --- Theming ---

readonly THEMING=(
    "gruvbox-theme|pkg|gruvbox-material-gtk-theme|-|-|0|Gruvbox Material GTK theme"
    "rofi-wayland|aur|rofi-lbonn-wayland-git|-|-|0|Rofi for Wayland (AUR)"
    "rofi-gruvbox|aur|rofi-material-icon-theme-git|-|-|0|Rofi Gruvbox Material icon theme"
    "sddm-dark|aur|sddm-sugar-dark|-|-|0|SDDM Sugar Dark theme"
)

# --- Applications ---

readonly APPLICATIONS=(
    "gimp|pkg|gimp|gimp|gimp|0|Image editor"
    "obs-studio|pkg|obs-studio|obs-studio|obs-studio|0|Video recording and streaming"
    "timeshift|pkg|timeshift|timeshift|-|0|System restore utility"
    "flameshot|pkg|flameshot|flameshot|flameshot|0|Screenshot tool"
    "copyq|pkg|copyq|copyq|copyq|0|Clipboard manager"
    "arc-browser|pkg|-|-|arc|0|Arc web browser (macOS)"
    "boring-notch|pkg|-|-|boring-notch|0|Hide notch (macOS, brew cask)"
    "battery-toolkit|pkg|-|-|battery-toolkit|0|Battery management (macOS, brew cask)"
    "middleclick|pkg|-|-|middleclick|0|Middle click emulation (macOS)"
)

# --- Audio & Media (Linux-focused) ---

readonly AUDIO_MEDIA=(
    "pipewire|pkg|pipewire|pipewire|pipewire|0|Low-latency audio engine"
    "wireplumber|pkg|wireplumber|wireplumber|wireplumber|0|PipeWire session manager"
    "ffmpeg|pkg|ffmpeg|ffmpeg|ffmpeg|0|Audio/video processing"
    "imagemagick|pkg|imagemagick|imagemagick|imagemagick|0|Image manipulation"
    "ghostscript|pkg|ghostscript|ghostscript|ghostscript|0|PDF/PostScript engine"
)

# --- Networking (Linux-focused) ---

readonly NETWORKING=(
    "networkmanager|pkg|networkmanager|network-manager|-|0|Network connection manager"
    "cloudflared|pkg|cloudflared|cloudflared|cloudflared|0|Cloudflare tunnel"
    "firewalld|pkg|firewalld|firewalld|-|0|Firewall management"
    "reflector|pkg|reflector|-|-|0|Pacman mirror optimizer"
)

# --- System Utilities ---

readonly SYSTEM=(
    "cronie|pkg|cronie|cron|cronie|1|Cron job scheduler"
    "unzip|pkg|unzip|unzip|unzip|1|ZIP archive extractor"
    "zip|pkg|zip|zip|zip|1|ZIP archive creator"
    "unrar|pkg|unrar|unrar|unrar|1|RAR archive extractor"
    "direnv|pkg|direnv|direnv|direnv|1|Directory-specific env loader"
    "tectonic|pkg|tectonic|tectonic|tectonic|1|Modern LaTeX engine"
)

# --- Map category names to their arrays ---

declare -A CATEGORY_MAP
CATEGORY_MAP["terminal_utils"]="TERMINAL_UTILITIES"
CATEGORY_MAP["terminal_emulators"]="TERMINAL_EMULATORS"
CATEGORY_MAP["dev_core"]="DEV_CORE"
CATEGORY_MAP["dev_runtimes"]="DEV_RUNTIMES"
CATEGORY_MAP["dev_lsp_tools"]="DEV_LSP_TOOLS"
CATEGORY_MAP["fonts"]="FONTS"
CATEGORY_MAP["theming"]="THEMING"
CATEGORY_MAP["applications"]="APPLICATIONS"
CATEGORY_MAP["audio_media"]="AUDIO_MEDIA"
CATEGORY_MAP["networking"]="NETWORKING"
CATEGORY_MAP["system"]="SYSTEM"

readonly CATEGORY_LABELS=(
    "terminal_utils|Terminal Utilities|Core CLI tools (fzf, ripgrep, htop, tmux, etc.)"
    "terminal_emulators|Terminal Emulators|Terminal emulator (kitty/ghostty)"
    "dev_core|Development - Core|Essential dev tools (git, docker, build tools)"
    "dev_runtimes|Development - Runtimes|Language runtimes (Go, Ruby, Rust, Java, etc.)"
    "dev_lsp_tools|Development - LSP Tools|LSP servers and formatters (terraform, sqlfluff, etc.)"
    "fonts|Fonts|Fira Code, Noto, DejaVu, and others"
    "theming|Theming|Gruvbox theme, Rofi/SDDM themes"
    "applications|Applications|GIMP, OBS, Flameshot, CopyQ, etc."
    "audio_media|Audio & Media|PipeWire, FFmpeg, ImageMagick"
    "networking|Networking|NetworkManager, Cloudflare Tunnel, firewall"
    "system|System Utilities|Cron, unzip, direnv, LaTeX engine"
)

# --- Desktop Environment definitions for radiolist ---

readonly DE_CHOICES=(
    "GNOME|GNOME Desktop Environment|off"
    "XFCE|XFCE Desktop Environment (lightweight)|off"
    "HYPRLAND|Hyprland Wayland Compositor|off"
    "NONE|Do not install a desktop environment|on"
)
