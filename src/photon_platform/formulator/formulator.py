"""
Formulator: A dynamic form builder in Python using Textual and YAML.

Formulator uses a YAML blueprint to generate an interactive form in the
terminal using the Textual library.  This script is capable of creating form
fields and buttons dynamically based on the blueprint, and performing basic
validation checks on the input values when the form is submitted. New
validation rules can be easily added as needed by creating new validation
methods.
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

from .modal import ErrorScreen


def load_blueprint(filename):
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data


class Formulator(App):
    CSS_PATH = "formulator.css"
    TITLE = "FORMULATOR"
    BINDINGS = [
        ("ctrl+s", "save", "save"),
        ("ctrl+q", "quit", "quit"),
    ]

    def __init__(self, form_blueprint):
        super().__init__()
        self.form_blueprint = form_blueprint
        self.field_ids = [id for id in form_blueprint["form"]["fields"]]
        self.title = self.form_blueprint["form"]["title"]

    def compose(self) -> ComposeResult:
        yield Header()
        with VerticalScroll(classes="form"):
            fields = self.form_blueprint["form"]["fields"]
            for field_id, field in fields.items():
                widget_type = field["type"]
                if widget_type == "Input":
                    yield Label(field["label"])
                    placeholder = field.get("placeholder", "")
                    print(f"{placeholder=}")
                    yield Input(id=field_id, placeholder=placeholder)
                elif widget_type == "Checkbox":
                    yield Label(field["label"])
                    option = field.get("option", "activate")
                    yield Checkbox(option, id=field_id)
                elif widget_type == "RadioSet":
                    yield Label(field["label"])
                    yield RadioSet(*field["options"], id=field_id)
                elif widget_type == "Select":
                    select_tuples = [
                        (label, id) for id, label in enumerate(field["options"])
                    ]
                    yield Label(field["label"])
                    yield Select(select_tuples, id=field_id)
                elif widget_type == "OptionList":
                    yield Label(field["label"])
                    yield OptionList(*field["options"], id=field_id)
                elif widget_type == "Switch":
                    yield Label(field["label"])
                    yield Switch(id=field_id)

        with Horizontal(classes="actions"):
            #  buttons = self.form_blueprint["form"]["buttons"]
            #  for button in buttons:
            #  yield Button(buttons[button]["label"], id=button)
            yield Button("save", id="save")
            yield Button("quit", id="quit")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "save":
            self.action_save()
        elif event.button.id == "quit":
            self.exit()

    def action_save(self):
        fields = self.form_blueprint["form"]["fields"]
        context = {}
        validation_errors = []

        for field_id in self.field_ids:
            field = fields[field_id]
            if field["type"] == "RadioSet":
                index = self.query_one(f"#{field_id}").pressed_index
                if index == -1:
                    value = (index, "")
                else:
                    value = (index, field["options"][index])

            else:
                value = self.query_one(f"#{field_id}").value
            print(field, value)
            context[field_id] = value

            # Perform validation checks
            if "validate" in fields[field_id]:
                validation_rules = fields[field_id]["validate"]
                for rule, rule_value in validation_rules.items():
                    validation_method_name = f"validate_{rule}"
                    if hasattr(self, validation_method_name):
                        validation_method = getattr(self, validation_method_name)
                        validation_method(
                            fields[field_id]["label"],
                            value,
                            validation_errors,
                            rule_value,
                        )

        # If there are validation errors, print or handle them as needed
        if validation_errors:
            #  print("Validation Errors:")
            #  for error in validation_errors:
                #  print(error)
            self.push_screen(ErrorScreen(validation_errors))
            
        else:
            #  print(context)  # Replace this line with code to use context as needed
            self.exit(context)

    def validate_required(self, field_label, value, validation_errors, required):
        if required and not value.strip():
            validation_errors.append(f"{field_label} is required.")

    def validate_min(self, field_label, value, validation_errors, min_value):
        if len(value) < min_value:
            validation_errors.append(
                f"{field_label} must be at least {min_value} characters long."
            )

    def validate_max(self, field_label, value, validation_errors, max_value):
        """Check if the value exceeds the maximum length."""
        if len(value) > max_value:
            validation_errors.append(
                f"{field_label} must be no more than {max_value} characters long."
            )

    def validate_email(self, field_label, value, validation_errors, is_email):
        """Check if the value is a valid email address."""
        if is_email:
            if "@" not in value or "." not in value:
                validation_errors.append(
                    f"{field_label} must be a valid email address."
                )

    def validate_numeric(self, field_label, value, validation_errors, is_numeric):
        """Check if the value is numeric."""
        if is_numeric and not value.isnumeric():
            validation_errors.append(f"{field_label} must be a numeric value.")

    def validate_alphabetic(self, field_label, value, validation_errors, is_alphabetic):
        """Check if the value is alphabetic."""
        if is_alphabetic and not value.isalpha():
            validation_errors.append(f"{field_label} must be an alphabetic value.")
