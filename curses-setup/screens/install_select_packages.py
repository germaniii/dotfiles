import curses
from .screen import BaseScreen
from constants.enums import DecoratedText, Screen
from constants.colors import get_color_pair
from constants.constants import HEADER_HEIGHT


class InstallSelectPackagesScreen(BaseScreen):
    def __init__(self, stdscr, items):
        self.stdscr = stdscr
        self.items = items
        self.current_row = 0

    def watch_input(self, current_screen):
        stdscr = self.stdscr
        key = stdscr.getch()

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
                current_screen = Screen.EXIT_CONFIRM

            self.current_row = 0

        return current_screen

    def print_menu(self) -> None:
        stdscr = self.stdscr
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        stdscr.attron(curses.color_pair(DecoratedText.ALERT.value))
        title = "Install Packages Selection"
        stdscr.addstr(0, w // 2 - (len(title) // 2), title)
        stdscr.attroff(curses.color_pair(DecoratedText.NORMAL.value))

        for idx, pkg in enumerate(self.items[0 : (h - HEADER_HEIGHT)]):
            x = 0
            y = HEADER_HEIGHT + idx

            if idx == self.current_row:
                stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                stdscr.addstr(y, x, pkg.name)
                stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            else:
                stdscr.addstr(y, x, pkg.name)

        stdscr.addstr(
            HEADER_HEIGHT, 10, self.items[self.current_row].description, curses.A_DIM
        )

        stdscr.refresh()

    def get_packages(self):
        if not len(self.items):
            return []

        return self.items
