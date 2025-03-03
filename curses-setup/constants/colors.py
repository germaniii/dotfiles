import curses
from constants.constants import colors


def init_colors():
    for id, fg, bg in colors:
        curses.init_pair(id, fg, bg)
