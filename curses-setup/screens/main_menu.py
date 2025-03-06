import curses
from .screen import BaseScreen
from constants.enums import Screen


class MainMenuScreen(BaseScreen):
    def __init__(self, scrmanager, stdscr, items):
        self.scrmanager = scrmanager
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
        elif key in (curses.KEY_ENTER, 10, 13, ord("l")):
            match self.current_row:
                case 0:
                    current_screen = Screen.INSTALL_SELECT_DE
                case 1:
                    current_screen = Screen.EXIT_CONFIRM

        return current_screen

    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        self.print_header(h, w, "MAIN MENU", "")
        self.print_scrollable_list(h, w, [a for a in self.items], self.current_row)

        self.stdscr.refresh()

    def get_packages(self):
        return super().get_packages()
