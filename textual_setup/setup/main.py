from textual.app import App
from screens.setup_wizard import SetupWizard
from screens.exit_confirmation import ExitConfirmation


WELCOME_TEXT = """
    Hello and welcome to the Setup Wizard!
    Press <Enter> to proceed
    Press <q> to exit
    """


class SetupApp(App[str]):

    CSS_PATH = "main.tcss"
    TITLE = "Linux Setup Helper"
    SUB_TITLE = "A TUI application to help you install your favorite software"

    BINDINGS = [
        ("q", "request_quit", "Quit"),
        ("enter", "request_proceed", "Proceed"),
        ("tab", "", "switch focus"),
        ("up", "", "up"),
        ("down", "", "down"),
        ("space", "", "select"),
    ]

    def on_mount(self) -> None:
        self.push_screen(SetupWizard())
        self.theme = "gruvbox"

    def action_request_quit(self):
        def is_exit(exit: bool | None):
            if exit:
                self.exit(return_code=0, message="Exited")

        self.push_screen(ExitConfirmation(), is_exit)

    def on_key(self, key):
        print(key)


if __name__ == "__main__":
    app = SetupApp()
    app.run()
