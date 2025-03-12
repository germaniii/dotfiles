import curses
from typing import cast
from setup.constants.classes import Package
from setup.constants.constants import (
    EXIT_CONFIRM,
    MAIN_MENU_ITEMS,
    DESKTOP_ENVIRONMENTS,
    TERMINAL_UTILITIES,
    ESSENTIAL_AUR_PACKAGES,
    FONT_PACKAGES,
)
from setup.constants.enums import Screen
from setup.screens import (
    BaseScreen,
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
    selected_packages: list[Package]
    screens: dict[Screen, BaseScreen | None]

    def __init__(self, stdscr: curses.window):
        self.selected_packages = []
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
                self.selected_packages,
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
            Screen.NONE: None,
        }

    def get_selected_packages(self):
        return self.selected_packages

    def set_selected_packages(self, packages: list[Package]):
        self.selected_packages = packages

    def get_screen(self, current_screen: Screen):
        return self.screens[current_screen]

    def append_selected_packages(self, packages: list[Package]):
        self.selected_packages.extend(packages)

    def remove_selected_package(self, selected_item: Package):
        self.selected_packages = [
            pkg for pkg in self.selected_packages if pkg.name != selected_item.name
        ]

    def set_summary_items(self):
        install_summary_screen = cast(
            SelectSummaryScreen, self.screens[Screen.INSTALL_SUMMARY]
        )
        install_process_screen = cast(
            SelectProcessScreen, self.screens[Screen.INSTALL_PROCESS]
        )

        install_summary_screen.items = self.selected_packages
        install_process_screen.items = self.selected_packages

    def append_error_items(self, packages: list[Package]):
        screen = cast(SelectCompleteScreen, self.screens[Screen.INSTALL_COMPLETE])
        screen.error_items.extend(packages)
