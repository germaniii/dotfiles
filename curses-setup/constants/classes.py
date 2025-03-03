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
    SELECTED = 1


class Screen(Enum):
    MAIN_MENU = 'main_menu'
    INSTALL_SELECT = 'install_select'
    INSTALL_SUMMARY = 'install_summary'
    INSTALL_CONFIRM = 'install_confirm'
    INSTALL_COMPLETE = 'install_complete'
    EXIT_CONFIRM = 'exit_confirm'


#####################################
# CLASSES
#####################################
class DesktopEnvironment:
    name = ""
    description = ""
    packages = []

    def __init__(self, name, description, packages):
        self.name = name
        self.description = description
        self.packages = packages

    def __eq__(self, other):
        return self.name == other.name


class Package:
    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description
