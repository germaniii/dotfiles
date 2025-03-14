from textual.app import App, ComposeResult
from textual import events
from textual.widgets import Header, Button, Label


class SetupApp(App[str]):

    CSS_PATH = "textual_main.tcss"
    COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",
    ]
    TITLE = "A Question App"
    SUB_TITLE = "The most important question"

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"

    def on_key(self, event: events.Key) -> None:
        if event.key.isdecimal():
            self.screen.styles.background = self.COLORS[int(event.key)]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Do you love Textual?", id="question")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "no":
            self.exit(return_code=4, message="Critical error occurred")
        else:
            self.exit(return_code=0, message="Thanks!")


if __name__ == "__main__":
    app = SetupApp()
    app.run()
