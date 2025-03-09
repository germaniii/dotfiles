import curses

from constants.colors import get_color_pair
from utils.install import install_package
from .screen import BaseScreen
from constants.enums import DecoratedText, Screen


class SelectProcessScreen(BaseScreen):
    def __init__(self, scrmanager, stdscr, items):
        self.scrmanager = scrmanager
        self.stdscr = stdscr
        self.items = items
        self.current_row = 0
        self.current_item = None
        self.success = False
        self.error = False

    def watch_input(self, current_screen):
        if self.success:
            current_screen = Screen.EXIT_CONFIRM
        elif self.error:
            current_screen = Screen.MAIN_MENU

        return current_screen

    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        try:
            if not self.success or not self.error:
                for index, package in enumerate(self.items):
                    self.stdscr.clear()
                    self.print_header(h, w, "INSTALLING", "")
                    super().print_menu()
                    self.stdscr.addstr(5, 0, "Installing package: " + package.name)
                    for progress_unit in range(len(self.items)):
                        if progress_unit <= index:
                            self.stdscr.attron(get_color_pair(DecoratedText.WARNING))
                            self.stdscr.addstr(h // 2, progress_unit, " ")
                            self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
                        else:
                            self.stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                            self.stdscr.addstr(h // 2, progress_unit, " ")
                            self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))

                    self.stdscr.refresh()
                    install_package(package)

            self.success = True
        except:
            self.stdscr.addstr(5, 0, "There was a problem")
            self.error = True
            self.items = []

        self.stdscr.refresh()
