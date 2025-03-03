import curses
from .screen import Screen
from constants.classes import DecoratedText


class MainMenu(Screen):
    stdcr = None
    items = []

    def __init__(self, stdscr, items):
        self.stdscr = stdscr
        self.items = items

    def watch_input(self, selected_row):
        return super().watch_input(selected_row)

    def print_menu(self, selected_row):
        stdscr = self.stdscr
        stdscr.clear()
        stdscr.attron(curses.color_pair(DecoratedText.ALERT.value))
        stdscr.addstr(0, 0, 'Main Menu')
        stdscr.attroff(curses.color_pair(DecoratedText.NORMAL.value))

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
