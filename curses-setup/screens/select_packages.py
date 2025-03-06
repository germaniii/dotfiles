import curses
from .screen import BaseScreen
from constants.enums import Screen
from constants.constants import HEADER_HEIGHT


class SelectPackagesScreen(BaseScreen):
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
        elif key in (curses.KEY_ENTER, 10, 13):
            self.scrmanager.append_selected_packages([self.items[self.current_row]])

        return current_screen

    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        self.print_header(h, w, "PACKAGE SELECTION", "")
        self.print_scrollable_list(
            h,
            w,
            [a.name for a in self.items],
            self.current_row,
        )
        self.print_description(
            HEADER_HEIGHT, 30, self.items[self.current_row].description
        )

        self.stdscr.refresh()

    def get_packages(self):
        if not len(self.items):
            return []

        return self.items
