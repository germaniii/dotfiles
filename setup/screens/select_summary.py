import curses
from .screen import BaseScreen
from constants.enums import Screen


class SelectSummaryScreen(BaseScreen):
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
            current_screen = Screen.INSTALL_SELECT_PKGS
        elif key in (curses.KEY_ENTER, 10, 13):
            current_screen = Screen.EXIT_CONFIRM

            self.current_row = 0

        return current_screen

    def print_menu(self) -> None:
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()
        item_names = [a.name for a in self.items]

        self.print_header(h, w, "INSTALL SUMMARY", "")
        self.print_wrapped_list(
            max_height=h,
            max_width=w,
            pos_y=0,
            pos_x=0,
            items=item_names,
            current_row=self.current_row,
        )

        super().print_menu()
        self.stdscr.refresh()
