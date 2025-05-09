from collections.abc import Sequence
import curses
from typing import cast
from setup.constants.classes import DesktopEnvironment, Package, ScreenManager
from setup.constants.colors import get_color_pair
from setup.constants.enums import DecoratedText, Screen
from setup.constants.constants import HEADER_HEIGHT


class BaseScreen:
    scrmanager: ScreenManager
    stdscr: curses.window
    items: Sequence[str | Package | DesktopEnvironment]
    current_row: int

    def __init__(
        self,
        scrmanager: ScreenManager,
        stdscr: curses.window,
        items: Sequence[str | Package | DesktopEnvironment],
    ):
        self.scrmanager = scrmanager
        self.stdscr = stdscr
        self.items = items
        self.current_row = 0

    def watch_input(self, current_screen: Screen) -> Screen:
        key = self.stdscr.getch()

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

    def print_menu(self):
        h, _ = self.stdscr.getmaxyx()
        controls = "<ENTER> Proceed  <h> Back/Left  <j> Down  <k> Up  <l> Proceed/Right <SPACE> Select Item"

        self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
        self.stdscr.addstr(h - 1, 0, controls)

    def print_wrapped_list(
        self,
        max_height: int,
        max_width: int,
        pos_y: int,
        pos_x: int,
        items: list[str],
        current_row: int,
    ):
        col_width = max(len(item) for item in items) + 2
        num_columns = max_width // col_width
        items_per_column = max_height - HEADER_HEIGHT - 2

        for idx, item in enumerate(items):
            col = idx // items_per_column
            row = idx % items_per_column
            x = pos_x + col * col_width
            y = pos_y - pos_y + HEADER_HEIGHT + row

            if col >= num_columns:
                break

            if idx == current_row:
                self.stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                self.stdscr.addstr(y, x, item)
                self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            else:
                self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
                self.stdscr.addstr(y, x, item)

    def print_scrollable_list(
        self,
        max_height: int,
        max_width: int,
        pos_y: int,
        pos_x: int,
        items: Sequence[str | Package | DesktopEnvironment],
        current_row: int,
    ):
        start_index = max(0, current_row - (max_height - HEADER_HEIGHT - 1))
        end_index = min(len(items), max_height + start_index - HEADER_HEIGHT)
        for idx, item in enumerate(items[start_index:end_index]):
            item = cast(str, item)
            x = pos_x + max_width - max_width
            y = pos_y
            if not pos_y:
                y = HEADER_HEIGHT + idx

            if idx == current_row - start_index:
                self.stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                self.stdscr.addstr(y, x, item)
                self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            elif len([a for a in self.scrmanager.selected_packages if a.name == item]):
                self.stdscr.attron(get_color_pair(DecoratedText.SELECTED))
                self.stdscr.addstr(y, x, item)
                self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            else:
                self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
                self.stdscr.addstr(y, x, item)

    def print_header(
        self,
        h: int,
        w: int,
        title: str,
        caption: str,
    ):
        x = h - h  # w // 2 - (len(title) // 2)
        y = w - w

        self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
        self.stdscr.addstr(y, x, title)
        self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))

        if len(caption):
            self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            self.stdscr.addstr(y + 1, x, caption)
            self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))

    def print_description(self, y: int, x: int, text: str):
        self.stdscr.addstr(y, x, text, curses.A_DIM)
