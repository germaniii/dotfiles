from constants.constants import EXIT_CONFIRM, MAIN_MENU_ITEMS, DESKTOP_ENVIRONMENTS
from constants.enums import Screen
from screens import MainMenuScreen, ExitConfirmScreen, InstallSelectDesktopScreen


class ScreenManager:
    main_menu = None
    install_select_de = None
    install_select_pkgs = None
    install_summary = None
    install_confirm = None
    install_complete = None
    exit_confirm = None

    def __init__(self, stdscr):
        self.main_menu = MainMenuScreen(stdscr, MAIN_MENU_ITEMS)
        self.install_select_de = InstallSelectDesktopScreen(
            stdscr, DESKTOP_ENVIRONMENTS
        )
        self.install_select_pkgs = None
        self.install_summary = None
        self.install_confirm = None
        self.install_complete = None
        self.exit_confirm = ExitConfirmScreen(stdscr, EXIT_CONFIRM)

    def get_screen(self, current_screen):
        match current_screen:
            case Screen.MAIN_MENU:
                return self.main_menu
            case Screen.INSTALL_SELECT_DE:
                return self.install_select_de
            case Screen.INSTALL_SELECT_PKGS:
                pass
            case Screen.INSTALL_SUMMARY:
                pass
            case Screen.INSTALL_CONFIRM:
                pass
            case Screen.INSTALL_COMPLETE:
                pass
            case Screen.EXIT_CONFIRM:
                return self.exit_confirm
