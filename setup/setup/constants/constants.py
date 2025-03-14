from .classes import (
    DesktopEnvironment,
    Package,
)
from .enums import (
    DE,
)

HEADER_HEIGHT = 2

MAIN_MENU_ITEMS = [
    "install",
    "exit",
]

EXIT_CONFIRM = [
    "yes",
    "no",
]

DESKTOP_ENVIRONMENTS = [
    DesktopEnvironment(
        DE.GNOME,
        "a desktop environment that aims to be simple and easy to use",
        [
            Package(
                "gnome",
                "a desktop environment that aims to be simple and easy to use",
            ),
        ],
    ),
    DesktopEnvironment(
        DE.XFCE,
        "a lightweight and modular desktop environment based on GTK",
        [
            Package(
                "xfce4",
                "a lightweight and modular desktop environment based on GTK",
            ),
            Package(
                "xfce4-goodies",
                "includes extra plugins and a number of useful utilities such as the mousepad editor.",
            ),
            Package(
                "x11vnc",
                "a VNC server, it allows remote access, view and control of real X displays (i.e. a display corresponding to a physical monitor, keyboard, and mouse) with any VNC viewer",
            ),
        ],
    ),
    DesktopEnvironment(
        DE.HYPRLAND,
        "an independent tiling Wayland compositor written in C++",
        [
            Package(
                "hyprland",
                "an independent tiling Wayland compositor written in C++",
            ),
            Package(
                "hyprpaper", "a fast, IPC-controlled wallpaper utility for Hyprland"
            ),
            Package(
                "hyprlock",
                "a simple, yet fast, multi-threaded and GPU-accelerated screen lock for Hyprland",
            ),
            Package(
                "xdg-desktop-portal-hyprland",
                "a program that lets other applications communicate with the compositor through D-Bus",
            ),
            Package(
                "waybar",
                "a GTK status bar made specifically for wlroots compositors and supports Hyprland by default",
            ),
            Package(
                "wlogout",
                "a simple, configurable, and lightweight logout manager for Wayland.",
            ),
            Package("kitty", "a modern, fast, and feature-rich terminal emulator."),
            Package("grim", "a Wayland screenshot utility."),
            Package("slurp", "a region selector for Wayland, often used with grim."),
            Package("dunst", "a lightweight notification daemon for X11 and Wayland."),
            Package(
                "polkit-kde-agent",
                "a KDE authentication agent for handling Polkit requests.",
            ),
            Package(
                "swaylock", "a screen locker for Wayland, commonly used with Sway."
            ),
            Package(
                "swayidle",
                "a Wayland idle management daemon, useful for screen locking.",
            ),
            Package("gdm", "The GNOME Display Manager, a graphical login interface."),
            Package(
                "brightnessctl", "a command-line tool to control screen brightness."
            ),
            Package(
                "acpi", "a utility to display battery, AC, and thermal information."
            ),
            Package(
                "poweralertd",
                "a daemon that monitors and alerts on power-related events.",
            ),
            Package(
                "blueman", "a Bluetooth management tool with a graphical interface."
            ),
            Package("copyq", "a clipboard manager with history and scripting support."),
            Package("wl-clipboard", "a command-line clipboard utility for Wayland."),
            Package(
                "sddm", "a lightweight and modern display manager for X11 and Wayland."
            ),
        ],
    ),
    DesktopEnvironment(
        DE.NONE,
        "Do not install any desktop environment",
        [],
    ),
]

TERMINAL_UTILITIES = [
    # Workflow Essentials
    Package("asdfg", "A command-line fuzzy finder for searching and filtering."),
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
