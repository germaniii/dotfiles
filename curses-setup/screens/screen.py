import curses
from constants.classes import DecoratedText


class Screen:
    items = []
    selected_row = 0

    def __init__(self, stdscr, items, selected_row):
        self.stdscr = stdscr
        self.items = items
        self.selected_row = selected_row

    def watch_input(self):
        key = self.stdscr.getch()

        if (key == curses.KEY_UP or ord('k')) and self.selected_row > 0:
            self.selected_row -= 1
        elif (key == curses.KEY_DOWN or ord('j')) and self.selected_row < len(self.items) - 1:
            self.selected_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            pass

    def print_menu(self):
        stdscr = self.stdscr
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for idx, row in enumerate(self.items):
            x = w//2 - len(row)//2
            y = h//2 - len(self.items)//2 + idx
            if idx == self.selected_row:
                stdscr.attron(curses.color_pair(DecoratedText.SELECTED.value))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(DecoratedText.NORMAL.value))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()
