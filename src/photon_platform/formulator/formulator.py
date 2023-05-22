"""
Formulator: A dynamic form builder in Python using Textual and YAML.

Formulator uses a YAML blueprint to generate an interactive form in the
terminal using the Textual library. This script dynamically creates form
fields and buttons based on the provided blueprint and performs validation
checks on the input values when the form is submitted. Users can easily add new
validation rules by adding new validation methods to the 'Validator' class.
"""
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
from rich.text import Text
from rich import print

from .modal import ErrorScreen
from .validator import Validator
from .composer import Composer


def load_blueprint(filename):
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data


class Formulator(App):
    """
    Formulator class that extends the App class from the Textual library.

    This class represents the application for creating a dynamic form from a
    YAML blueprint. It also includes methods for handling events such as button
    presses and saving form data.
    """

    CSS_PATH = "formulator.css"
    TITLE = "FORMULATOR"
    BINDINGS = [
        ("ctrl+s", "save", "save"),
        ("ctrl+p", "screenshot", "screenshot"),
        ("ctrl+q", "quit", "quit"),
    ]

    def __init__(self, form_blueprint, validator=None, composer=None):
        """
        Initializes the Formulator application with the given form blueprint and Validator instance.

        :param form_blueprint: A dictionary representing the form blueprint.
        :param validator: An instance of a Validator subclass to be used for validating form fields.
        If none is provided, the default Validator is used.
        """
        super().__init__()
        self.form_blueprint = form_blueprint
        self.title = self.form_blueprint["form"]["title"]
        self.validator = validator if validator else Validator()
        self.composer = composer if composer else Composer(form_blueprint)

    def compose(self) -> ComposeResult:
        return self.composer.compose()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler called when a button is pressed.

        If the 'Save' button is pressed, it calls the action_save method to validate
        and save the form data. If the 'Quit' button is pressed, it exits the application.
        """
        if event.button.id == "save":
            self.action_save()
        elif event.button.id == "quit":
            self.exit()

    def action_save(self):
        """
        Method called when the 'Save' button is pressed.

        This method retrieves and validates the data from the form fields, then
        either displays validation errors or returns the form data and exits the
        application.
        """

        fields = self.form_blueprint["form"]["fields"]
        context = {}
        validation_errors = []

        for field_id, field in fields.items():
            if field["type"] == "RadioSet":
                index = self.query_one(f"#{field_id}").pressed_index
                if index == -1:
                    value = (index, "")
                else:
                    value = (index, field["options"][index])

            else:
                value = self.query_one(f"#{field_id}").value
            context[field_id] = value

            # Perform validation checks
            if "validate" in field:
                validation_rules = field["validate"]
                field_label = field["label"]
                for rule, rule_value in validation_rules.items():
                    if hasattr(self.validator, rule):
                        validation_method = getattr(self.validator, rule)
                        validation_method(
                            field_label, value, validation_errors, rule_value
                        )

        if validation_errors:
            self.push_screen(ErrorScreen(validation_errors))

        else:
            self.exit(context)

    def action_screenshot(self, path: str = "./") -> None:
        """
        Save an SVG "screenshot". This action will save an SVG file containing
        the current contents of the screen.

        Args:
            filename (str | None, optional): Filename of screenshot, or None to auto-generate. Defaults to None.
            path (str, optional): Path to directory. Defaults to "./".
        """
        self.bell()

        form_id = self.form_blueprint["form"]["id"]
        filename = f'{form_id}.svg'
        path = self.save_screenshot(filename, path)

        message = Text.assemble("Screenshot saved to ", (f"'{path}'", "bold green"))
        print(message)
        #  self.add_note(message)
        #  self.screen.mount(Notification(message))

