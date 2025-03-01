from constants.classes import DesktopEnvironment, Package
from constants.enums import DE

DESKTOP_ENVIRONMENTS = [
    DesktopEnvironment(
        DE.GNOME,
        "The Complete GNOME Desktop Environment",
        [
            Package(
                "gnome",
                "contains the base GNOME desktop and the well-integrated core applications",
            ),
        ],
    ),
    DesktopEnvironment(
        DE.XFCE,
        "",
        [
            Package("xfce4", ""),
            Package("xfce4-goodies", ""),
            Package("x11vnc", ""),
        ],
    ),
    DesktopEnvironment(
        DE.HYPRLAND,
        "",
        [
            Package("hyprland", ""),
            Package("hyprpaper", ""),
            Package("hyprlock", ""),
            Package("xdg-desktop-portal-hyprland", ""),
            Package("wlogout", ""),
            Package("waybar", ""),
            Package("kitty", ""),
            Package("grim", ""),
            Package("slurp", ""),
            Package("dunst", ""),
            Package("polkit-kde-agent", ""),
            Package("swaylock", ""),
            Package("swayidle", ""),
            Package("gdm", ""),
            Package("brightnessctl", ""),
            Package("acpi", ""),
            Package("poweralertd", ""),
            Package("blueman", ""),
            Package("copyq", ""),
            Package("wl-clipboard", ""),
            Package("sddm", ""),
        ],
    ),
]

TERMINAL_UTILITIES = [
    # Workflow Essentials
    Package("fzf", ""),
    Package("ripgrep", ""),
    Package("sed", ""),
    Package("neovim", ""),
    Package("tmux", ""),
    Package("ack", ""),
    Package("ranger", ""),
    Package("htop", ""),
    Package("fd", ""),
    Package("fastfetch", ""),
    Package("entr", ""),  # tmux dep
    # Networking Essentials
    Package("wget", ""),  # Remote content retrieval
    Package("curl", ""),  # Remote content retrieval
    Package("ntp", ""),  # Network Time Protocol to set time via network.
    Package("networkmanager", ""),
    Package("cloudflared", ""),
    Package("firewalld", ""),
    Package("reflector", ""),
    # Programming essentials
    Package("base-devel", ""),
    Package("git", ""),
    Package("docker", ""),
    Package("docker-compose", ""),
    # Audio Essentials
    Package("pipewire", ""),
    Package("wireplumber", ""),
    # Additional but not Optional
    Package("cronie", ""),  # cron jobs
    Package("unrar", ""),  # RAR compression program
    Package("unzip", ""),  # Zip compression program
    Package("zip", ""),  # Zip compression program
]

ESSENTIAL_AUR_PACKAGES = [
    Package("tmux-plugin-manager", ""),
    Package("tmux-ttf-fira-code", ""),
    Package("tmux-ttf-font-awesome", ""),
]

FONT_PACKAGES = [
    Package("ttf-freefont", ""),
    Package("ttf-ms-fonts", ""),
    Package("ttf-linux-libertine", ""),
    Package("ttf-dejavu", ""),
    Package("ttf-inconsolata", ""),
    Package("ttf-ubuntu-font-family", ""),
    Package("noto-fonts-cjk", ""),
    Package("noto-fonts-emoji", ""),
    Package("noto-fonts", ""),
]

FONT_PACKAGES = [
    Package("ttf-freefont", ""),
    Package("ttf-ms-fonts", ""),
    Package("ttf-linux-libertine", ""),
    Package("ttf-dejavu", ""),
    Package("ttf-inconsolata", ""),
    Package("ttf-ubuntu-font-family", ""),
    Package("noto-fonts-cjk", ""),
    Package("noto-fonts-emoji", ""),
    Package("noto-fonts", ""),
]

ADDITIONAL_THEMING_PACKAGES = [
    Package("rofi-lbonn-wayland-git", ""),
    Package("rofi-lgruvbox-material-icon-theme-git", ""),
    Package("rofi-lgruvbox-material-gtk-theme-git", ""),
    Package("rofi-lsddm-sugar-dark", ""),
]

ADDITIONAL_APPLICATION_PACKAGES = [
    Package("obs-studio", ""),
    Package("wlrobs-hg", ""),  # Used in OBS Studio and Screen Sharing
    Package("timeshift", ""),  # Backup and Restore
]
