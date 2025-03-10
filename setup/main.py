import curses
from constants.colors import init_colors
from constants.classes import Screen, ScreenManager

# Curses Init
stdscr = curses.initscr()
curses.noecho()  # dont echo keystrokes
curses.cbreak()  # dont wait for enter, handle keys immediately
curses.start_color()
curses.curs_set(0)
init_colors()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr) -> None:
    current_screen = Screen.MAIN_MENU
    screen_manager = ScreenManager(stdscr)

    while 1:
        if not current_screen:
            break

        menu = screen_manager.get_screen(current_screen)
        if not menu:
            break

        # Print Screen
        menu.print_menu()

        screen = menu.watch_input(current_screen)
        current_screen = screen

    # eof
    stdscr.keypad(0)


# Run main loop
curses.wrapper(main)

# Curses DeInit
curses.nocbreak()
curses.echo()
curses.endwin()
