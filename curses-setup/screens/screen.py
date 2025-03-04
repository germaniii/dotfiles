import curses
from constants.colors import DecoratedText, get_color_pair


class BaseScreen:
    stdcr = None
    items = []
    current_row = 0

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
            self.current_row = 0

        return current_screen

    def print_menu(self) -> None:
        stdscr = self.stdscr
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(self.items):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(self.items) // 2 + idx
            if idx == self.current_row:
                stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                stdscr.addstr(y, x, row)
                stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()
