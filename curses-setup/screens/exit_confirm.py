import curses
from typing import Tuple
from .screen import BaseScreen
from constants.classes import DecoratedText, Screen


class ExitConfirmScreen(BaseScreen):
    def __init__(self, stdscr, items):
        self.stdscr = stdscr
        self.items = items

    def watch_input(self, current_row, current_screen) -> Tuple:
        stdscr = self.stdscr
        key = stdscr.getch()

        if key in (curses.KEY_UP, ord('k')) and current_row > 0:
            current_row -= 1
        elif (key in (curses.KEY_DOWN, ord('j'))
              and current_row < len(self.items) - 1):
            current_row += 1
        elif key in (curses.KEY_ENTER, 10, 13):
            match current_row:
                case 0:
                    current_screen = None
                case 1:
                    current_screen = Screen.MAIN_MENU

        return (current_row, current_screen)

    def print_menu(self, current_row) -> None:
        stdscr = self.stdscr
        stdscr.clear()

        stdscr.attron(curses.color_pair(DecoratedText.ALERT.value))
        stdscr.addstr(0, 0, 'Exit Confirmation')
        stdscr.attroff(curses.color_pair(DecoratedText.NORMAL.value))

        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(self.items):
            x = w//2 - len(row)//2
            y = h//2 - len(self.items)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(DecoratedText.SELECTED.value))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(DecoratedText.NORMAL.value))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()
