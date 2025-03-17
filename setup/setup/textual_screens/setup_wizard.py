from typing import cast
from textual import on
from textual.app import ComposeResult
from textual.events import Mount
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import (
    Button,
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


class SetupWizard(Screen):
    CSS_PATH = "setup_wizard.tcss"
    BINDINGS = [
        ("g", "select_all", "Select All Packages"),
        ("G", "deselect_all", "Deselect All Packages"),
    ]

    desktop_selection = []
    package_selection = [
        *TERMINAL_UTILITIES,
    ]
    installation_confirmed = False

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer(show_command_palette=True)
        with TabbedContent(id="tab_content_setup_wizard"):
            # desktop_environment_selection"
            with TabPane(id=TABS[0][0], title=TABS[0][1]):
                with Horizontal():
                    yield SelectionList[int](
                        *[(de[0], de[0]) for de in DESKTOP_ENVIRONMENTS],
                        id="selection_list_desktop",
                    )
                    with VerticalScroll(id="vertical_scroll_desktop"):
                        yield Pretty([], id="pretty_desktop")
            # "package_selection"
            with TabPane(id=TABS[1][0], title=TABS[1][1]):
                with Horizontal():
                    yield SelectionList[int](
                        *[(pack[0], pack[0]) for pack in PACKAGES],
                        id="selection_list_package",
                    )
                    with VerticalScroll(id="vertical_scroll_desktop"):
                        yield Pretty([], id="pretty_package")
            # "install_confirmation"
            with TabPane(id=TABS[2][0], title=TABS[2][1]):
                with VerticalScroll(id="vertical_scroll_install_confirmation"):
                    yield Pretty(
                        [*self.package_selection, *self.desktop_selection],
                        id="pretty_install_confirmation",
                    )
                    yield Button(id="button_confirm", label="CONFIRM")
            # "install_processing"
            with TabPane(id=TABS[3][0], title=TABS[3][1], disabled=True):
                yield Static(id=TABS[3][0], content=TABS[3][1])
            # "install_summary"
            with TabPane(id=TABS[4][0], title=TABS[4][1], disabled=True):
                yield Static(id=TABS[4][0], content=TABS[4][1])

    def on_mount(self):
        self.query_one("#pretty_desktop").border_title = "Selected packages"
        self.query_one("#pretty_package").border_title = "Selected packages"
        self.query_one("#pretty_install_confirmation").border_title = (
            "Selected packages"
        )

    def set_selected_desktop_environment(self):
        selection_list = cast(
            SelectionList,
            self.query_one("#selection_list_desktop"),
        )
        pretty = cast(Pretty, self.query_one("#pretty_desktop"))

        selected_desktops = [
            de for de in DESKTOP_ENVIRONMENTS if de[0] in selection_list.selected
        ]
        selected_desktop_packages = [
            pkg[0] + " - " + pkg[1] for de in selected_desktops for pkg in de[1]
        ]

        pretty.update(selected_desktop_packages)
        self.desktop_selection = selected_desktop_packages

    def set_selected_packages(self):
        selection_list = cast(
            SelectionList,
            self.query_one("#selection_list_package"),
        )
        pretty = cast(Pretty, self.query_one("#pretty_package"))

        selected_package_names = selection_list.selected
        selected_packages = [
            pkg[0] + " - " + pkg[1]
            for pkg in PACKAGES
            if pkg[0] in selected_package_names
        ]

        pretty.update(selected_packages)
        self.package_selection = selected_packages

    def action_select_all(self):
        selection_list = cast(
            SelectionList,
            self.query_one("#selection_list_package"),
        )
        selection_list.select_all()
        self.package_selection = PACKAGES

    def action_deselect_all(self):
        selection_list = cast(
            SelectionList,
            self.query_one("#selection_list_package"),
        )
        selection_list.deselect_all()
        self.package_selection = []

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "button_confirm":
            tabbed_content = cast(
                TabbedContent,
                self.query_one("#tab_content_setup_wizard"),
            )

            tabbed_content.disable_tab("desktop_environment_selection")
            tabbed_content.disable_tab("package_selection")
            tabbed_content.disable_tab("install_confirmation")
            tabbed_content.enable_tab("install_processing")
            tabbed_content.active = "install_processing"
            self.installation_confirmed = True

    @on(Mount)
    @on(SelectionList.SelectedChanged)
    def update_selected_view(self) -> None:
        pretty_install_confirm = cast(
            Pretty,
            self.query_one("#pretty_install_confirmation"),
        )
        tabbed_content = cast(
            TabbedContent,
            self.query_one("#tab_content_setup_wizard"),
        )

        self.set_selected_desktop_environment()
        self.set_selected_packages()
        selected_packages = [*self.desktop_selection, *self.package_selection]
        pretty_install_confirm.update(selected_packages)

        if len(selected_packages):
            tabbed_content.enable_tab("install_confirmation")
        else:
            tabbed_content.disable_tab("install_confirmation")
