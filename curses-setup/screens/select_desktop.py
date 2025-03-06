import curses
from .screen import BaseScreen
from constants.enums import Screen
from constants.constants import HEADER_HEIGHT


class SelectDesktopScreen(BaseScreen):
    def __init__(self, stdscr, items):
        self.stdscr = stdscr
        self.items = items
        self.current_row = 0

    def watch_input(self, current_screen):
        key = self.stdscr.getch()

        if key in (curses.KEY_UP, ord("k")) and self.current_row > 0:
            self.current_row -= 1
        elif (
            key in (curses.KEY_DOWN, ord("j"))
            and self.current_row < len(self.items) - 1
        ):
            self.current_row += 1
        elif key in (curses.KEY_ENTER, 10, 13):
            if self.current_row == len(self.items) - 1:
                current_screen = Screen.MAIN_MENU
            else:
                current_screen = Screen.INSTALL_SELECT_PKGS

            self.current_row = 0

        return current_screen

    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        self.print_header(h, w, "DESKTOP Environment SELECTION", "")
        self.print_scrollable_list(
            h, w, [a.name.value for a in self.items], self.current_row
        )

        if not len(self.items[self.current_row].packages):
            title = "*No Desktop Environment will be installed*"
            x = 10
            y = HEADER_HEIGHT
            self.stdscr.addstr(y, x, title, curses.A_DIM)
        else:
            for idx, pkg in enumerate(self.items[self.current_row].packages):
                x = 10
                y = HEADER_HEIGHT + idx
                self.print_description(y, x, "-" + pkg.name)

        self.stdscr.refresh()

    def get_packages(self):
        if not len(self.items[self.current_row].packages):
            return []

        return self.items[self.current_row].packages
