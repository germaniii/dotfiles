import curses
from constants.classes import (
    DecoratedText,
    DE,
    DesktopEnvironment,
    Package,
)


COLORS = [
    (DecoratedText.NORMAL.value, curses.COLOR_BLACK, curses.COLOR_WHITE),
    (DecoratedText.ALERT.value, curses.COLOR_RED, curses.COLOR_WHITE),
    (DecoratedText.WARNING.value, curses.COLOR_BLACK, curses.COLOR_YELLOW),
]

DESKTOP_ENVIRONMENT_DICT = {
    DE.GNOME: DesktopEnvironment(
        DE.GNOME,
        "a desktop environment that aims to be simple and easy to use",
        [
            Package(
                "gnome",
                "a desktop environment that aims to be simple and easy to use",
            ),
        ],
    ),
    DE.XFCE: DesktopEnvironment(
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
    DE.HYPRLAND: DesktopEnvironment(
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
    DE.NONE: DesktopEnvironment(
        DE.NONE,
        "Do not install any desktop environment",
        [],
    ),
}
