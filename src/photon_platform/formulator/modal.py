from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.widgets import (
    Button,
    Input,
    Label,
    Checkbox,
    RadioSet,
    RadioButton,
    Select,
    Static,
    Switch,
    OptionList,
    Header,
    Footer,
)
from textual.containers import Grid, VerticalScroll, Horizontal

class ErrorScreen(ModalScreen):
    """Screen with a dialog to quit."""

    def __init__(self, errors: list):
        super().__init__()
        self._errors = errors

    def compose(self) -> ComposeResult:
        yield Grid(
            Static(str(self._errors), id="errors"),
            Button("OK", variant="error", id="ok"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()

