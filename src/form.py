from textual.app import App, ComposeResult
from textual.widgets import Button, Input, Label, Header, Footer
from textual.containers import VerticalScroll, Horizontal


class FormTestApp(App):
    CSS_PATH = "form.css"
    TITLE = "FORM title"
    BINDINGS = [
        ("ctrl+s", "save", "save"),
        ("ctrl+q", "quit", "quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(classes="form"):
            yield Label("First Name")
            yield Input(id="first-name")
            yield Label("Last Name")
            yield Input(id="last-name")
        with Horizontal(classes="actions"):
            yield Button("Save", id="save")
            yield Button("Quit", id="quit")
        yield Footer()


if __name__ == "__main__":
    app = FormTestApp()
    app.run()
