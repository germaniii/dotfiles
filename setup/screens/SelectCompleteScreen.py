from collections.abc import Sequence
import curses
from typing import override
from setup.constants.classes import DesktopEnvironment, Package, ScreenManager
from setup.constants.colors import get_color_pair
from .BaseScreen import BaseScreen
from setup.constants.enums import DecoratedText, Screen


class SelectCompleteScreen(BaseScreen):
    scrmanager: ScreenManager
    stdscr: curses.window
    items: Sequence[str | Package | DesktopEnvironment]
    current_row: int

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
        self.error_items: list[Package] = []

    @override
    def watch_input(self, current_screen: Screen):
        _ = self.stdscr.getch()
        current_screen = Screen.EXIT_CONFIRM
        return current_screen

    @override
    def print_menu(self) -> None:
        self.stdscr.clear()
        h, _ = self.stdscr.getmaxyx()

        self.stdscr.addstr(5, 0, "There was a problem")
        for package in self.error_items:
            self.stdscr.attron(get_color_pair(DecoratedText.ALERT))
            self.stdscr.addstr(h // 2, 0, package.name)
            self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))

        self.stdscr.refresh()
