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
        selected_item = self.items[self.current_row]
        selected_packages = self.scrmanager.data["selected_packages"]

        if key in (curses.KEY_UP, ord("k")) and self.current_row > 0:
            self.current_row -= 1
        elif (
            key in (curses.KEY_DOWN, ord("j"))
            and self.current_row < len(self.items) - 1
        ):
            self.current_row += 1
        elif (
            key in (curses.A_LEFT, ord("h")) and self.current_row < len(self.items) - 1
        ):
            self.scrmanager.data["selected_packages"] = []
            current_screen = Screen.INSTALL_SELECT_DE
        elif key in (curses.KEY_ENTER, 10, 13, ord("l")):
            if len(
                [pkg for pkg in selected_packages if pkg.name == selected_item.name]
            ):
                self.scrmanager.remove_selected_package(selected_item)
            else:
                self.scrmanager.append_selected_packages([selected_item])

        return current_screen

    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        self.print_header(h, w, "PACKAGE SELECTION", "")
        self.print_scrollable_list(
            h,
            0,
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
