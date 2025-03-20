TABS = [
    ("desktop_environment_selection", "Desktop Environment Selection"),
    ("package_selection", "Package Selection"),
    ("install_confirmation", "Install Confirmation"),
    ("install_processing", "Install Process"),
    ("install_summary", "Installation Summary"),
]

DESKTOP_ENVIRONMENTS = [
    (
        "GNOME",
        [
            (
                "gnome",
                "a desktop environment that aims to be simple and easy to use",
            ),
        ],
    ),
    (
        "XFCE",
        [
            (
                "xfce4",
                "a lightweight and modular desktop environment based on GTK",
            ),
            (
                "xfce4-goodies",
                "includes extra plugins and a number of useful utilities such as the mousepad editor.",
            ),
            (
                "x11vnc",
                "a VNC server, it allows remote access, view and control of real X displays (i.e. a display corresponding to a physical monitor, keyboard, and mouse) with any VNC viewer",
            ),
        ],
    ),
    (
        "HYPRLAND",
        [
            (
                "hyprland",
                "an independent tiling Wayland compositor written in C++",
            ),
            ("hyprpaper", "a fast, IPC-controlled wallpaper utility for Hyprland"),
            (
                "hyprlock",
                "a simple, yet fast, multi-threaded and GPU-accelerated screen lock for Hyprland",
            ),
            (
                "xdg-desktop-portal-hyprland",
                "a program that lets other applications communicate with the compositor through D-Bus",
            ),
            (
                "waybar",
                "a GTK status bar made specifically for wlroots compositors and supports Hyprland by default",
            ),
            (
                "wlogout",
                "a simple, configurable, and lightweight logout manager for Wayland.",
            ),
            ("kitty", "a modern, fast, and feature-rich terminal emulator."),
            ("grim", "a Wayland screenshot utility."),
            ("slurp", "a region selector for Wayland, often used with grim."),
            ("dunst", "a lightweight notification daemon for X11 and Wayland."),
            (
                "polkit-kde-agent",
                "a KDE authentication agent for handling Polkit requests.",
            ),
            ("swaylock", "a screen locker for Wayland, commonly used with Sway."),
            (
                "swayidle",
                "a Wayland idle management daemon, useful for screen locking.",
            ),
            ("gdm", "The GNOME Display Manager, a graphical login interface."),
            ("brightnessctl", "a command-line tool to control screen brightness."),
            ("acpi", "a utility to display battery, AC, and thermal information."),
            (
                "poweralertd",
                "a daemon that monitors and alerts on power-related events.",
            ),
            ("blueman", "a Bluetooth management tool with a graphical interface."),
            ("copyq", "a clipboard manager with history and scripting support."),
            ("wl-clipboard", "a command-line clipboard utility for Wayland."),
            ("sddm", "a lightweight and modern display manager for X11 and Wayland."),
        ],
    ),
]

TERMINAL_UTILITIES = [
    # Workflow Essentials
    ("asdfg", "A command-line fuzzy finder for searching and filtering.", True),
    ("fzf", "A command-line fuzzy finder for searching and filtering.", True),
    ("ripgrep", "A fast, recursive search tool, similar to grep.", True),
    ("sed", "A stream editor for filtering and transforming text.", True),
    ("neovim", "A modern, extensible Vim-based text editor.", True),
    ("tmux", "A terminal multiplexer for managing multiple sessions.", True),
    ("ack", "A search tool optimized for programmers, similar to grep.", True),
    ("ranger", "A terminal file manager with VI key bindings.", True),
    ("htop", "An interactive process viewer and system monitor.", True),
    ("fd", "A faster alternative to 'find' for searching files.", True),
    ("fastfetch", "A lightweight system information tool, similar to neofetch.", True),
    (
        "entr",
        "A utility to run commands when files change (dependency for tmux).",
        True,
    ),
    # Networking Essentials
    ("wget", "A command-line tool for retrieving files from the web.", True),
    ("curl", "A tool for transferring data from or to a server.", True),
    ("ntp", "A daemon for synchronizing the system clock over a network.", True),
    ("networkmanager", "A utility for managing network connections.", True),
    ("cloudflared", "A Cloudflare utility for creating secure tunnels.", True),
    ("firewalld", "A firewall management tool with D-Bus interface.", True),
    (
        "reflector",
        "A tool to update the Pacman mirror list with the fastest mirrors.",
        True,
    ),
    # Programming Essentials
    (
        "base-devel",
        "A group of essential development tools, including make and gcc.",
        True,
    ),
    ("git", "A distributed version control system.", True),
    ("docker", "A containerization platform for running isolated applications.", True),
    (
        "docker-compose",
        "A tool for defining and running multi-container Docker applications.",
    ),
    # Audio Essentials
    ("pipewire", "A low-latency audio and video processing engine.", True),
    ("wireplumber", "A session manager for PipeWire.", True),
    # Additional but not Optional
    ("cronie", "A daemon to schedule and run cron jobs.", True),
    ("unrar", "A utility for extracting RAR archives.", True),
    ("unzip", "A tool for extracting ZIP archives.", True),
    ("zip", "A tool for creating ZIP archives.", True),
]

ESSENTIAL_AUR_PACKAGES = [
    ("tmux-plugin-manager", "A plugin manager for tmux."),
]

FONT_PACKAGES = [
    ("ttf-freefont", "A collection of high-quality TrueType fonts."),
    ("ttf-ms-fonts", "A collection of Microsoft TrueType fonts."),
    ("ttf-linux-libertine", "A high-quality serif font for Linux."),
    ("ttf-dejavu", "An improved font family based on the Vera fonts."),
    ("ttf-inconsolata", "A monospaced font for programming."),
    ("ttf-ubuntu-font-family", "The Ubuntu font family."),
    ("noto-fonts-cjk", "CJK font support for Noto Fonts."),
    ("noto-fonts-emoji", "Emoji font support for Noto Fonts."),
    ("noto-fonts", "A font family with wide Unicode coverage."),
]

ADDITIONAL_THEMING_PACKAGES = [
    ("rofi-lbonn-wayland-git", "A Wayland-compatible version of Rofi."),
    ("rofi-lgruvbox-material-icon-theme-git", "Gruvbox Material icon theme for Rofi."),
    ("rofi-lgruvbox-material-gtk-theme-git", "Gruvbox Material GTK theme for Rofi."),
    ("rofi-lsddm-sugar-dark", "A dark theme for SDDM."),
]

ADDITIONAL_APPLICATION_PACKAGES = [
    (
        "obs-studio",
        "A powerful open-source software for video recording and streaming.",
    ),
    ("wlrobs-hg", "A Wayland screen capture plugin for OBS Studio."),
    ("timeshift", "A system restore utility for Linux."),
]

PACKAGES = [
    *TERMINAL_UTILITIES,
    *ESSENTIAL_AUR_PACKAGES,
    *FONT_PACKAGES,
    *ADDITIONAL_THEMING_PACKAGES,
    *ADDITIONAL_APPLICATION_PACKAGES,
]
