import curses
from setup.constants.classes import ScreenManager
from setup.constants.colors import init_colors
from setup.constants.enums import Screen

# Curses Init
stdscr = curses.initscr()
curses.noecho()  # dont echo keystrokes
curses.cbreak()  # dont wait for enter, handle keys immediately
curses.start_color()
_ = curses.curs_set(0)
init_colors()


def print_center(stdscr: curses.window, text: str):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr: curses.window) -> None:
    current_screen = Screen.MAIN_MENU
    screen_manager = ScreenManager(stdscr)

    while 1:
        menu = screen_manager.get_screen(current_screen)
        if not menu:
            break

        # Print Screen
        menu.print_menu()

        screen = menu.watch_input(current_screen)
        current_screen = screen

    # end of loop


# Run main loop
curses.wrapper(main)

# Curses DeInit
curses.nocbreak()
curses.echo()
curses.endwin()
