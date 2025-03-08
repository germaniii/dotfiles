from enum import Enum


#####################################
# ENUMS
#####################################
class DE(Enum):
    GNOME = "gnome"
    XFCE = "xfce4"
    HYPRLAND = "hyprland"
    NONE = "none"


class DecoratedText(Enum):
    NORMAL = 1
    ALERT = 2
    WARNING = 3
    SELECTED = 4
    DISABLED = 5
    ACTIVE = 6


class Screen(Enum):
    MAIN_MENU = "main_menu"
    INSTALL_SELECT_DE = "install_select_de"
    INSTALL_SELECT_PKGS = "install_select_pkgs"
    INSTALL_SUMMARY = "install_summary"
    INSTALL_CONFIRM = "install_confirm"
    INSTALL_PROCESS = "install_process"
    INSTALL_COMPLETE = "install_complete"
    EXIT_CONFIRM = "exit_confirm"
