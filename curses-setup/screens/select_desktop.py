import curses
from .screen import BaseScreen
from constants.enums import Screen
from constants.constants import HEADER_HEIGHT


class SelectDesktopScreen(BaseScreen):
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
        elif (
            key in (curses.KEY_LEFT, ord("h"))
            and self.current_row < len(self.items) - 1
        ):
            current_screen = Screen.MAIN_MENU
            self.scrmanager.data["selected_packages"] = []
        elif key in (curses.KEY_ENTER, 10, 13, ord("l")):
            current_screen = Screen.INSTALL_SELECT_PKGS
            self.scrmanager.set_selected_desktopenv(self.items[self.current_row].name)
            self.scrmanager.append_selected_packages(
                self.items[self.current_row].packages
            )

            self.current_row = 0

        return current_screen

    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        self.print_header(h, w, "DESKTOP ENVIRONMENT SELECTION", "")
        self.print_scrollable_list(
            h, w, 0, 0, [a.name.value for a in self.items], self.current_row
        )

        if not len(self.items[self.current_row].packages):
            title = "*No Desktop Environment will be installed*"
            self.print_description(HEADER_HEIGHT, 10, title)
        else:
            self.print_scrollable_list(
                max_height=h,
                max_width=w,
                pos_y=0,
                pos_x=40,
                items=[a.name for a in self.items[self.current_row].packages],
                current_row=0,
            )

        super().print_menu()
        self.stdscr.refresh()

    def get_packages(self):
        if not len(self.items[self.current_row].packages):
            return []

        return self.items[self.current_row].packages
