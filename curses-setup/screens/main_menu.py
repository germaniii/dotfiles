import curses
from .screen import Screen
from constants.classes import DecoratedText


class MainMenu(Screen):
    stdcr = None
    items = []
    selected_row = ""

    def __init__(self, stdscr, items, selected_row):
        self.stdscr = stdscr
        self.items = items
        self.selected_row = selected_row

    def watch_input(self):
        return super().watch_input()

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
