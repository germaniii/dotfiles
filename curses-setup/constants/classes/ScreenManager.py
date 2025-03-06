from constants.constants import (
    EXIT_CONFIRM,
    MAIN_MENU_ITEMS,
    DESKTOP_ENVIRONMENTS,
    TERMINAL_UTILITIES,
    ESSENTIAL_AUR_PACKAGES,
    FONT_PACKAGES,
)
from constants.enums import DE, Screen
from screens import (
    MainMenuScreen,
    ExitConfirmScreen,
    SelectDesktopScreen,
    SelectPackagesScreen,
)


class ScreenManager:
    screens = {
        Screen.MAIN_MENU: None,
        Screen.INSTALL_SELECT_DE: None,
        Screen.INSTALL_SELECT_PKGS: None,
        Screen.INSTALL_SUMMARY: None,
        Screen.INSTALL_CONFIRM: None,
        Screen.INSTALL_COMPLETE: None,
        Screen.EXIT_CONFIRM: None,
    }

    def __init__(self, stdscr):
        self.screens = {
            Screen.MAIN_MENU: MainMenuScreen(
                self,
                stdscr,
                MAIN_MENU_ITEMS,
            ),
            Screen.INSTALL_SELECT_DE: SelectDesktopScreen(
                self,
                stdscr,
                DESKTOP_ENVIRONMENTS,
            ),
            Screen.INSTALL_SELECT_PKGS: SelectPackagesScreen(
                self,
                stdscr,
                [
                    *TERMINAL_UTILITIES,
                    *ESSENTIAL_AUR_PACKAGES,
                    *FONT_PACKAGES,
                ],
            ),
            Screen.INSTALL_SUMMARY: None,
            Screen.INSTALL_CONFIRM: None,
            Screen.INSTALL_COMPLETE: None,
            Screen.EXIT_CONFIRM: ExitConfirmScreen(
                self,
                stdscr,
                EXIT_CONFIRM,
            ),
        }
        self.data = {
            "selected_packages": [],
            "selected_desktopenv": DE.NONE,
        }

    def get_screen(self, current_screen):
        return self.screens[current_screen]

    def append_selected_packages(self, packages):
        self.data["selected_packages"].append(*packages)

    def set_selected_desktopenv(self, de):
        self.data["selected_desktopenv"] = de
