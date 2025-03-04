import curses
from constants.colors import init_colors
from constants.classes import Screen
from constants.constants import EXIT_CONFIRM, MAIN_MENU_ITEMS, DESKTOP_ENVIRONMENTS
from screens import MainMenuScreen, ExitConfirmScreen, InstallSelectDesktopScreen

# Curses Init
stdscr = curses.initscr()
curses.noecho()  # dont echo keystrokes
curses.cbreak()  # dont wait for enter, handle keys immediately
curses.start_color()
curses.curs_set(0)
init_colors()


def get_screen(stdscr, current_screen):
    match current_screen:
        case Screen.MAIN_MENU:
            return MainMenuScreen(stdscr, MAIN_MENU_ITEMS)
        case Screen.INSTALL_SELECT_DE:
            return InstallSelectDesktopScreen(stdscr, DESKTOP_ENVIRONMENTS)
        case Screen.INSTALL_SELECT_PKGS:
            pass
        case Screen.INSTALL_SUMMARY:
            pass
        case Screen.INSTALL_CONFIRM:
            pass
        case Screen.INSTALL_COMPLETE:
            pass
        case Screen.EXIT_CONFIRM:
            return ExitConfirmScreen(stdscr, EXIT_CONFIRM)


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr) -> None:
    current_screen = Screen.MAIN_MENU
    current_row = 0

    menu = get_screen(stdscr, current_screen)
    if menu:
        menu.print_menu(current_row)

    while 1:
        menu = get_screen(stdscr, current_screen)
        if not menu:
            break

        # Print Screen
        menu.print_menu(current_row)

        row, screen = menu.watch_input(current_row, current_screen)
        current_row = row
        current_screen = screen

    # eof
    stdscr.keypad(0)


# Run main loop
curses.wrapper(main)

# Curses DeInit
curses.nocbreak()
curses.echo()
curses.endwin()
