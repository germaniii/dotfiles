import curses
from constants.colors import init_colors
from constants.classes import Screen
from screens import MainMenu


def print_screen(stdscr, current_screen, selected_row):
    match current_screen:
        case Screen.MAIN_MENU:
            return MainMenu(stdscr, [], selected_row)
        case Screen.INSTALL_SELECT:
            pass
        case Screen.INSTALL_SUMMARY:
            pass
        case Screen.INSTALL_CONFIRM:
            pass
        case Screen.INSTALL_COMPLETE:
            pass
        case Screen.EXIT_CONFIRM:
            pass


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    init_colors()

    current_screen = Screen.MAIN_MENU
    current_row = 0

    print_screen(stdscr, current_screen, current_row)

    while 1:
        menu = print_screen(stdscr, current_screen, current_row)
        if not menu:
            break

        menu.print_menu()
        menu.watch_input()

    # eof
    stdscr.keypad(0)


curses.wrapper(main)
curses.nocbreak()
curses.echo()
curses.endwin()
