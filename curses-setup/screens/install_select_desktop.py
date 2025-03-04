import curses
from .screen import BaseScreen
from constants.enums import DecoratedText, Screen
from constants.colors import get_color_pair


class InstallSelectDesktopScreen(BaseScreen):
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

        stdscr.attron(curses.color_pair(DecoratedText.ALERT.value))
        stdscr.addstr(0, 0, "Install Desktop Environment Selection")
        stdscr.attroff(curses.color_pair(DecoratedText.NORMAL.value))

        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(self.items):
            x = w // 4 - len(row.name.value)
            y = h // 2 - len(self.items) // 2 + idx
            if idx == self.current_row:
                stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                stdscr.addstr(y, x, row.name.value)
                stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            else:
                stdscr.addstr(y, x, row.name.value)

        if not len(self.items[self.current_row].packages):
            x = w // 3
            y = h // 2
            stdscr.addstr(y, x, "No Desktop Environment will be installed")
        else:
            for idx, pkg in enumerate(self.items[self.current_row].packages):
                x = w // 3
                y = h // 2 - len(self.items[self.current_row].packages) // 2 + idx
                stdscr.addstr(y, x, "- " + pkg.name)

        stdscr.refresh()

    def get_packages(self):
        if not len(self.items[self.current_row].packages):
            return []

        return self.items[self.current_row].packages
