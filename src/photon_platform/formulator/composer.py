import yaml
from textual.app import App, ComposeResult
from textual.widgets import (
    Button,
    Input,
    Label,
    Checkbox,
    RadioSet,
    RadioButton,
    Select,
    Switch,
    OptionList,
    Header,
    Footer,
)
from textual.containers import VerticalScroll, Horizontal

class Composer:
    """
    The Composer class is used to dynamically create a form using a YAML blueprint and the Textual library.

    This class takes a form blueprint as input and uses it to generate the structure and components
    of the form. Each form field and button in the blueprint is translated into a corresponding
    widget in the Textual library.

    The compose method iterates over the form fields and buttons in the blueprint, creating and
    yielding the corresponding Textual widget for each one. These widgets are then used to construct
    the form in the Textual application.

    Users can extend this class to implement their own form layouts and custom widgets. To use a
    custom Composer class, simply pass an instance of it to the Formulator constructor.

    Attributes:
        blueprint: The YAML blueprint that describes the form to be generated.
    """
    def __init__(self, form_blueprint):
        self.form_blueprint = form_blueprint

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(classes="form"):
            fields = self.form_blueprint["form"]["fields"]
            for field_id, field in fields.items():
                yield from self.create_widget(field_id, field)

        with Horizontal(classes="actions"):
            yield Button("save", id="save")
            yield Button("quit", id="quit")

        yield Footer()

    def create_widget(self, field_id, field):
        widget_type = field["type"]

        # Create the appropriate widget based on its type
        if widget_type == "Input":
            yield from self.create_input(field_id, field)
        elif widget_type == "Checkbox":
            yield from self.create_checkbox(field_id, field)
        elif widget_type == "RadioSet":
            yield from self.create_radioset(field_id, field)
        elif widget_type == "Select":
            yield from self.create_select(field_id, field)
        elif widget_type == "OptionList":
            yield from self.create_optionlist(field_id, field)
        elif widget_type == "Switch":
            yield from self.create_switch(field_id, field)

    def create_input(self, field_id, field):
        yield Label(field["label"])
        placeholder = field.get("placeholder", "")
        yield Input(id=field_id, placeholder=placeholder)

    def create_checkbox(self, field_id, field):
        yield Label(field["label"])
        option = field.get("option", "activate")
        yield Checkbox(option, id=field_id)

    def create_radioset(self, field_id, field):
        yield Label(field["label"])
        yield RadioSet(*field["options"], id=field_id)

    def create_select(self, field_id, field):
        select_tuples = [(label, id) for id, label in enumerate(field["options"])]
        yield Label(field["label"])
        yield Select(select_tuples, id=field_id)

    def create_optionlist(self, field_id, field):
        yield Label(field["label"])
        yield OptionList(*field["options"], id=field_id)

    def create_switch(self, field_id, field):
        yield Label(field["label"])
        yield Switch(id=field_id)
class Formulator(App):
    def __init__(self, form_blueprint, validator=None, composer=None):
        super().__init__()
        self.form_blueprint = form_blueprint
        self.title = self.form_blueprint["form"]["title"]
        self.validator = validator if validator else Validator()
        self.composer = composer if composer else Composer(form_blueprint)

    def compose(self) -> ComposeResult:
        return self.composer.compose()

    # The rest of the Formulator methods...

