import curses
from typing import Tuple
from constants.colors import DecoratedText, get_color_pair


class BaseScreen:
    stdcr = None
    items = []

    def __init__(self, stdscr, items):
        self.stdscr = stdscr
        self.items = items

    def watch_input(self, current_row, current_screen) -> Tuple:
        stdscr = self.stdscr
        key = stdscr.getch()

        if key in (curses.KEY_UP, ord("k")) and current_row > 0:
            current_row -= 1
        elif key in (curses.KEY_DOWN, ord("j")) and current_row < len(self.items) - 1:
            current_row += 1
        elif key in (curses.KEY_ENTER, 10, 13):
            current_row = 0

        return (current_row, current_screen, ...)

    def print_menu(self, current_row) -> None:
        stdscr = self.stdscr
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(self.items):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.items) // 2 + idx
            if idx == current_row:
                stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                stdscr.addstr(y, x, row)
                stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()
