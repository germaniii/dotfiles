from textual import on
from textual.app import ComposeResult
from textual.events import Mount
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import (
    Footer,
    Header,
    Pretty,
    SelectionList,
    Static,
    TabPane,
    TabbedContent,
)
from textual.screen import Screen

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


class SetupWizard(Screen):
    CSS_PATH = "setup_wizard.tcss"

    desktop_selection = []
    package_selection = []
    installation_confirmed = False

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer(show_command_palette=True)
        with TabbedContent(id="tab_content_setup_wizard"):
            # ("desktop_environment_selection", "Desktop Environment Selection")
            with TabPane(id=TABS[0][0], title=TABS[0][1]):
                with Horizontal():
                    yield SelectionList[int](
                        *[(de[0], de[0]) for de in DESKTOP_ENVIRONMENTS],
                        id="selection_list_desktop"
                    )
                    with VerticalScroll():
                        yield Pretty([], id="pretty_desktop")
            # ("package_selection", "Package Selection")
            with TabPane(id=TABS[1][0], title=TABS[1][1]):
                yield Static(id=TABS[1][0], content=TABS[1][1])
            # ("install_confirmation", "Install Confirmation")
            with TabPane(id=TABS[2][0], title=TABS[2][1]):
                yield Static(id=TABS[2][0], content=TABS[2][1])
            # ("install_processing", "Install Process")
            with TabPane(id=TABS[3][0], title=TABS[3][1], disabled=True):
                yield Static(id=TABS[3][0], content=TABS[3][1])
            # ("install_summary", "Installation Summary")
            with TabPane(id=TABS[4][0], title=TABS[4][1], disabled=True):
                yield Static(id=TABS[4][0], content=TABS[4][1])

    def on_mount(self):
        self.query_one(Pretty).border_title = "Selected packages"

    @on(Mount)
    @on(SelectionList.SelectedChanged)
    def update_selected_view(self) -> None:
        selected_desktop_names = self.query_one("#selection_list_desktop").selected
        selected_desktops = [
            de for de in DESKTOP_ENVIRONMENTS if de[0] in selected_desktop_names
        ]
        selected_packages = [
            pkg[0] + " - " + pkg[1] for de in selected_desktops for pkg in de[1]
        ]
        self.query_one("#pretty_desktop").update(selected_packages)
        self.desktop_selection = selected_packages

        if len(selected_desktops):
            self.query_one("#tab_content_setup_wizard").enable_tab(
                "install_confirmation"
            )
        else:
            self.query_one("#tab_content_setup_wizard").disable_tab(
                "install_confirmation"
            )
