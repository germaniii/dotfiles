import curses
from constants.enums import (
    DecoratedText,
)


color_arr = [
    (DecoratedText.NORMAL.value, curses.COLOR_WHITE, curses.COLOR_BLACK),
    (DecoratedText.ALERT.value, curses.COLOR_BLACK, curses.COLOR_RED),
    (DecoratedText.WARNING.value, curses.COLOR_BLACK, curses.COLOR_YELLOW),
    (DecoratedText.SELECTED.value, curses.COLOR_BLACK, curses.COLOR_GREEN),
    (DecoratedText.DISABLED.value, curses.COLOR_WHITE, curses.COLOR_BLACK),
    (DecoratedText.ACTIVE.value, curses.COLOR_BLACK, curses.COLOR_WHITE),
]


def init_colors():
    for id, fg, bg in color_arr:
        curses.init_pair(id, fg, bg)


def get_color_pair(pair_id):
    return curses.color_pair(pair_id.value)
