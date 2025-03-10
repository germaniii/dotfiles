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
    SelectSummaryScreen,
    SelectConfirmScreen,
    SelectProcessScreen,
    SelectCompleteScreen,
)


class ScreenManager:
    screens = {
        Screen.MAIN_MENU: None,
        Screen.INSTALL_SELECT_DE: None,
        Screen.INSTALL_SELECT_PKGS: None,
        Screen.INSTALL_SUMMARY: None,
        Screen.INSTALL_CONFIRM: None,
        Screen.INSTALL_PROCESS: None,
        Screen.INSTALL_COMPLETE: None,
        Screen.EXIT_CONFIRM: None,
    }

    def __init__(self, stdscr):
        self.data = {
            "selected_packages": [],
            "selected_desktopenv": DE.NONE,
        }
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
            Screen.INSTALL_SUMMARY: SelectSummaryScreen(
                self,
                stdscr,
                self.data["selected_packages"],
            ),
            Screen.INSTALL_CONFIRM: SelectConfirmScreen(
                self,
                stdscr,
                EXIT_CONFIRM,
            ),
            Screen.INSTALL_PROCESS: SelectProcessScreen(self, stdscr, []),
            Screen.INSTALL_COMPLETE: SelectCompleteScreen(self, stdscr, []),
            Screen.EXIT_CONFIRM: ExitConfirmScreen(
                self,
                stdscr,
                EXIT_CONFIRM,
            ),
        }

    def get_screen(self, current_screen):
        return self.screens[current_screen]

    def append_selected_packages(self, packages):
        self.data["selected_packages"].extend(packages)

    def remove_selected_package(self, selected_item):
        self.data["selected_packages"] = [
            pkg
            for pkg in self.data["selected_packages"]
            if pkg.name != selected_item.name
        ]

    def set_selected_desktopenv(self, de):
        self.data["selected_desktopenv"] = de

    def set_summary_items(self):
        self.screens[Screen.INSTALL_SUMMARY].items = self.data["selected_packages"]
        self.screens[Screen.INSTALL_PROCESS].items = self.data["selected_packages"]

    def append_error_items(self, packages):
        self.screens[Screen.INSTALL_COMPLETE].error_items.extend(packages)
