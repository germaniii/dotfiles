from constants.colors import get_color_pair
from .screen import BaseScreen
from constants.enums import DecoratedText, Screen


class SelectCompleteScreen(BaseScreen):
    def __init__(self, scrmanager, stdscr, items):
        self.scrmanager = scrmanager
        self.stdscr = stdscr
        self.items = items
        self.current_row = 0
        self.error_items = []

    def watch_input(self, current_screen):
        self.stdscr.getch()
        current_screen = Screen.EXIT_CONFIRM
        return current_screen

    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        self.stdscr.addstr(5, 0, "There was a problem")
        for package in self.error_items:
            self.stdscr.attron(get_color_pair(DecoratedText.ALERT))
            self.stdscr.addstr(h // 2, 0, package.name)
            self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))

        self.stdscr.refresh()
