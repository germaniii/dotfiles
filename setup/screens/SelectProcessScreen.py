from collections.abc import Sequence
import curses
import subprocess
from typing import cast, override

from setup.constants.classes import DesktopEnvironment, Package, ScreenManager
from setup.constants.colors import get_color_pair
from setup.screens.SelectCompleteScreen import SelectCompleteScreen
from setup.utils.install import install_package
from .BaseScreen import BaseScreen
from setup.constants.enums import DecoratedText, Screen


class SelectProcessScreen(BaseScreen):
    scrmanager: ScreenManager
    stdscr: curses.window
    items: Sequence[str | Package | DesktopEnvironment]
    current_row: int
    success: bool
    error: bool

    def __init__(
        self,
        scrmanager: ScreenManager,
        stdscr: curses.window,
        items: Sequence[Package],
    ):
        super().__init__(scrmanager, stdscr, items)
        self.scrmanager = scrmanager
        self.stdscr = stdscr
        self.items = items
        self.current_row = 0
        self.success = False
        self.error = False

    @override
    def watch_input(self, current_screen: Screen):
        current_screen = Screen.INSTALL_COMPLETE
        return current_screen

    @override
    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        if not self.success or not self.error:
            for index, package in enumerate(self.items):
                package = cast(Package, package)
                self.stdscr.clear()
                self.print_header(h, w, "INSTALLING", "")
                super().print_menu()
                self.stdscr.addstr(5, 0, "Installing package: " + package.name)

                for progress_unit in range(len(self.items)):
                    if progress_unit <= index:
                        unit = cast(Package, self.items[progress_unit])
                        name = unit.name
                        screen = cast(
                            SelectCompleteScreen,
                            self.scrmanager.screens[Screen.INSTALL_COMPLETE],
                        )

                        # FIX: Not Working
                        if name in [a.name for a in screen.error_items]:
                            self.stdscr.attron(get_color_pair(DecoratedText.ALERT))
                            self.stdscr.addstr(h // 2, progress_unit, " ")
                            self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
                        else:
                            self.stdscr.attron(get_color_pair(DecoratedText.WARNING))
                            self.stdscr.addstr(h // 2, progress_unit, " ")
                            self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
                    else:
                        self.stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                        self.stdscr.addstr(h // 2, progress_unit, " ")
                        self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))

                self.stdscr.refresh()

                try:
                    install_package(package)
                except subprocess.CalledProcessError:
                    self.scrmanager.append_error_items([package])
            # rof

            self.success = True

        self.stdscr.refresh()
