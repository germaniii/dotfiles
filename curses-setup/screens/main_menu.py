import curses
from .screen import BaseScreen
from constants.enums import DecoratedText, Screen
from constants.colors import get_color_pair


class MainMenuScreen(BaseScreen):
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
            match self.current_row:
                case 0:
                    current_screen = Screen.INSTALL_SELECT_DE
                case 1:
                    current_screen = Screen.EXIT_CONFIRM

        return current_screen

    def print_menu(self) -> None:
        stdscr = self.stdscr
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        stdscr.attron(curses.color_pair(DecoratedText.ALERT.value))
        title = "Main Menu"
        stdscr.addstr(0, w // 2 - (len(title) // 2), title)
        stdscr.attroff(curses.color_pair(DecoratedText.NORMAL.value))

        for idx, row in enumerate(self.items):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.items) // 2 + idx
            if idx == self.current_row:
                stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                stdscr.addstr(y, x, row)
                stdscr.attron(get_color_pair(DecoratedText.DISABLED))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()

    def get_packages(self):
        return super().get_packages()
