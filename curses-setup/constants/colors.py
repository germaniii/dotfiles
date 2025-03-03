import curses
from constants.constants import COLORS


def init_colors():
    for id, fg, bg in COLORS:
        curses.init_pair(id, fg, bg)
