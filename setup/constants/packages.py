from constants.enums import Package
from constants.enums import DE, DESKTOP_ENVIRONMENT_DICT

DESKTOP_ENVIRONMENTS = [
    DESKTOP_ENVIRONMENT_DICT[DE.GNOME],
    DESKTOP_ENVIRONMENT_DICT[DE.XFCE],
    DESKTOP_ENVIRONMENT_DICT[DE.HYPRLAND],
    DESKTOP_ENVIRONMENT_DICT[DE.NONE],
]

TERMINAL_UTILITIES = [
    # Workflow Essentials
    Package("fzf", "A command-line fuzzy finder for searching and filtering."),
    Package("ripgrep", "A fast, recursive search tool, similar to grep."),
    Package("sed", "A stream editor for filtering and transforming text."),
    Package("neovim", "A modern, extensible Vim-based text editor."),
    Package("tmux", "A terminal multiplexer for managing multiple sessions."),
    Package("ack", "A search tool optimized for programmers, similar to grep."),
    Package("ranger", "A terminal file manager with VI key bindings."),
    Package("htop", "An interactive process viewer and system monitor."),
    Package("fd", "A faster alternative to 'find' for searching files."),
    Package("fastfetch", "A lightweight system information tool, similar to neofetch."),
    Package(
        "entr", "A utility to run commands when files change (dependency for tmux)."
    ),
    # Networking Essentials
    Package("wget", "A command-line tool for retrieving files from the web."),
    Package("curl", "A tool for transferring data from or to a server."),
    Package("ntp", "A daemon for synchronizing the system clock over a network."),
    Package("networkmanager", "A utility for managing network connections."),
    Package("cloudflared", "A Cloudflare utility for creating secure tunnels."),
    Package("firewalld", "A firewall management tool with D-Bus interface."),
    Package(
        "reflector", "A tool to update the Pacman mirror list with the fastest mirrors."
    ),
    # Programming Essentials
    Package(
        "base-devel", "A group of essential development tools, including make and gcc."
    ),
    Package("git", "A distributed version control system."),
    Package("docker", "A containerization platform for running isolated applications."),
    Package(
        "docker-compose",
        "A tool for defining and running multi-container Docker applications.",
    ),
    # Audio Essentials
    Package("pipewire", "A low-latency audio and video processing engine."),
    Package("wireplumber", "A session manager for PipeWire."),
    # Additional but not Optional
    Package("cronie", "A daemon to schedule and run cron jobs."),
    Package("unrar", "A utility for extracting RAR archives."),
    Package("unzip", "A tool for extracting ZIP archives."),
    Package("zip", "A tool for creating ZIP archives."),
]

ESSENTIAL_AUR_PACKAGES = [
    Package("tmux-plugin-manager", "A plugin manager for tmux."),
    Package("tmux-ttf-fira-code", "A Fira Code font package for tmux."),
    Package("tmux-ttf-font-awesome", "A Font Awesome package for tmux."),
]

FONT_PACKAGES = [
    Package("ttf-freefont", "A collection of high-quality TrueType fonts."),
    Package("ttf-ms-fonts", "A collection of Microsoft TrueType fonts."),
    Package("ttf-linux-libertine", "A high-quality serif font for Linux."),
    Package("ttf-dejavu", "An improved font family based on the Vera fonts."),
    Package("ttf-inconsolata", "A monospaced font for programming."),
    Package("ttf-ubuntu-font-family", "The Ubuntu font family."),
    Package("noto-fonts-cjk", "CJK font support for Noto Fonts."),
    Package("noto-fonts-emoji", "Emoji font support for Noto Fonts."),
    Package("noto-fonts", "A font family with wide Unicode coverage."),
]

ADDITIONAL_THEMING_PACKAGES = [
    Package("rofi-lbonn-wayland-git", "A Wayland-compatible version of Rofi."),
    Package(
        "rofi-lgruvbox-material-icon-theme-git", "Gruvbox Material icon theme for Rofi."
    ),
    Package(
        "rofi-lgruvbox-material-gtk-theme-git", "Gruvbox Material GTK theme for Rofi."
    ),
    Package("rofi-lsddm-sugar-dark", "A dark theme for SDDM."),
]

ADDITIONAL_APPLICATION_PACKAGES = [
    Package(
        "obs-studio",
        "A powerful open-source software for video recording and streaming.",
    ),
    Package("wlrobs-hg", "A Wayland screen capture plugin for OBS Studio."),
    Package("timeshift", "A system restore utility for Linux."),
]
