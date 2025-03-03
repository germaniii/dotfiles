import curses
from constants.classes import DecoratedText


class Screen:
    stdcr = None
    items = []

    def __init__(self, stdscr, items):
        self.stdscr = stdscr
        self.items = items

    def watch_input(self, selected_row):
        stdscr = self.stdscr
        key = stdscr.getch()

        if (key == curses.KEY_UP or ord('k')) and selected_row > 0:
            selected_row -= 1
        elif ((key == curses.KEY_DOWN or ord('j'))
              and selected_row < len(self.items) - 1):
            selected_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            selected_row = 0

        return selected_row

    def print_menu(self, selected_row):
        stdscr = self.stdscr
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(self.items):
            x = w//2 - len(row)//2
            y = h//2 - len(self.items)//2 + idx
            if idx == selected_row:
                stdscr.attron(curses.color_pair(DecoratedText.SELECTED.value))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(DecoratedText.NORMAL.value))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()
