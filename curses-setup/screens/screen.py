import curses
from constants.colors import DecoratedText, get_color_pair
from constants.constants import HEADER_HEIGHT


class BaseScreen:
    stdcr = None
    scrmanager = None
    items = []
    current_row = 0

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
        elif key in (curses.KEY_ENTER, 10, 13):
            self.current_row = 0

        return current_screen

    def print_menu(self):
        h, w = self.stdscr.getmaxyx()
        controls = "<ENTER> Proceed  <h> Back/Left  <j> Down  <k> Up  <l> Proceed/Right"

        self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
        self.stdscr.addstr(h - 1, 0, controls)

    def get_packages(self):
        return []

    def print_scrollable_list(
        self, max_height, max_width, pos_y, pos_x, items, current_row
    ):
        start_index = max(0, current_row - (max_height - HEADER_HEIGHT - 1))
        end_index = min(len(items), max_height + start_index - HEADER_HEIGHT)
        for idx, item in enumerate(items[start_index:end_index]):
            x = pos_x
            y = pos_y
            if not pos_y:
                y = HEADER_HEIGHT + idx

            if idx == current_row - start_index:
                self.stdscr.attron(get_color_pair(DecoratedText.ACTIVE))
                self.stdscr.addstr(y, x, item)
                self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            elif len(
                [a for a in self.scrmanager.data["selected_packages"] if a.name == item]
            ):
                self.stdscr.attron(get_color_pair(DecoratedText.SELECTED))
                self.stdscr.addstr(y, x, item)
                self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
            else:
                self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
                self.stdscr.addstr(y, x, item)

    def print_header(self, h, w, title, caption):
        x = 0  # w // 2 - (len(title) // 2)
        y = 0

        self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))
        self.stdscr.addstr(y, x, title)
        self.stdscr.attron(get_color_pair(DecoratedText.NORMAL))

    def print_description(self, y, x, text):
        self.stdscr.addstr(y, x, text, curses.A_DIM)
