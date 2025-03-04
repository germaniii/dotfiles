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
    INSTALL_COMPLETE = "install_complete"
    EXIT_CONFIRM = "exit_confirm"


#####################################
# CLASSES
#####################################
class DesktopEnvironment:
    name = DE.NONE
    description = ""
    packages = []

    def __init__(self, name, description, packages):
        self.name = name
        self.description = description
        self.packages = packages

    def __eq__(self, other):
        return self.name.value == other.name.value


class Package:
    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description
