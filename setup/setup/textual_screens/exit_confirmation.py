from textual.app import ComposeResult
from textual.widgets import Button, Label
from textual.containers import Grid
from textual.screen import ModalScreen


class ExitConfirmation(ModalScreen):
    CSS_PATH = "exit_confirmation.tcss"
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="error", id="yes"),
            Button("Cancel", variant="primary", id="no"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "no":
            self.dismiss(False)
        else:
            self.dismiss(True)
