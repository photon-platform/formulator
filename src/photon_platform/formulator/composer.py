
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
    TextArea,
    MaskedInput,
    SelectionList,
    DirectoryTree,
    Tree,
    DataTable,
    ListView,
    ListItem,
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
            buttons_config = self.form_blueprint["form"].get("buttons", {})
            for button_id, button_spec in buttons_config.items():
                label = button_spec.get("label")
                if not label:
                    raise ValueError(f"Button '{button_id}' in YAML must have a 'label'.")
                
                variant = button_spec.get("variant", "default")
                # Textual Button variants: "default", "primary", "success", "warning", "error"
                # No explicit validation here, Textual will handle/default if variant is invalid.
                
                action_name = button_spec.get("action", None) 
                disabled = button_spec.get("disabled", False)
                # 'compact' is not a direct constructor argument for textual.Button
                # and is typically handled by CSS or custom button classes.
                # It will be ignored here for standard Button.

                yield Button(label=label, id=button_id, variant=variant, name=action_name, disabled=disabled)

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
        elif widget_type == "TextArea":
            yield from self.create_textarea(field_id, field)
        elif widget_type == "MaskedInput":
            yield from self.create_maskedinput(field_id, field)
        elif widget_type == "SelectionList":
            yield from self.create_selectionlist(field_id, field)
        elif widget_type == "DirectoryTree":
            yield from self.create_directorytree(field_id, field)
        elif widget_type == "Tree":
            yield from self.create_tree(field_id, field)
        elif widget_type == "DataTable":
            yield from self.create_datatable(field_id, field)
        elif widget_type == "ListView":
            yield from self.create_listview(field_id, field)

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

    def create_textarea(self, field_id, field):
        yield Label(field["label"])
        text = field.get("text", "")
        language = field.get("language", None)
        theme = field.get("theme", "css")
        soft_wrap = field.get("soft_wrap", True)
        read_only = field.get("read_only", False)
        show_line_numbers = field.get("show_line_numbers", False)
        tab_behavior = field.get("tab_behavior", "focus")
        indent_width = field.get("indent_width", 4)
        yield TextArea(
            text=text,
            id=field_id,
            language=language,
            theme=theme,
            soft_wrap=soft_wrap,
            read_only=read_only,
            show_line_numbers=show_line_numbers,
            tab_behavior=tab_behavior,
            indent_width=indent_width,
        )

    def create_maskedinput(self, field_id, field):
        yield Label(field["label"])
        if "template" not in field:
            raise ValueError("MaskedInput requires a 'template' attribute.")
        template = field["template"]
        placeholder = field.get("placeholder", "")
        password = field.get("password", False)
        restrict = field.get("restrict", None)
        # 'type' is a property of Input, not MaskedInput directly, but can be used by Input parent
        # However, MaskedInput does not inherit 'type' in the same way.
        # We will not pass 'type' to MaskedInput.
        max_length = field.get("max_length", 0)
        validators = field.get("validators", None)
        validate_on = field.get("validate_on", ("blur", "changed", "submitted"))
        valid_empty = field.get("valid_empty", False)

        yield MaskedInput(
            template=template,
            id=field_id,
            placeholder=placeholder,
            password=password,
            restrict=restrict,
            max_length=max_length,
            validators=validators,
            validate_on=validate_on,
            valid_empty=valid_empty,
        )

    def create_selectionlist(self, field_id, field):
        yield Label(field["label"])
        
        options_data = field.get("options", [])
        processed_options = []
        for option in options_data:
            if not isinstance(option, (list, tuple)):
                raise ValueError(f"Each option for SelectionList '{field_id}' must be a list or tuple.")
            if len(option) < 2 or len(option) > 3:
                raise ValueError(
                    f"Each option for SelectionList '{field_id}' must have 2 or 3 elements: "
                    f"(prompt, value, [initial_selected_state]). Found: {option}"
                )
            
            prompt = option[0]
            value = option[1]
            initial_state = option[2] if len(option) == 3 else False
            processed_options.append((prompt, value, initial_state))

        disabled = field.get("disabled", False)
        compact = field.get("compact", False)
        
        yield SelectionList(
            *processed_options,
            id=field_id,
            disabled=disabled,
            compact=compact
        )

    def create_directorytree(self, field_id, field):
        yield Label(field["label"])
        path = field.get("path", ".")
        show_root = field.get("show_root", True)
        disabled = field.get("disabled", False)
        yield DirectoryTree(
            path=path,
            id=field_id,
            show_root=show_root,
            disabled=disabled
        )

    def _add_nodes_to_tree(self, parent_textual_node, nodes_data_list):
        for node_data in nodes_data_list:
            label = node_data.get("label")
            if label is None:
                # Or handle more gracefully, e.g., skip or use a default label
                raise ValueError("Node 'label' is required for Tree widget.")
            
            data = node_data.get("data", None)
            children_data = node_data.get("children", [])
            
            new_textual_node = parent_textual_node.add(label, data=data)
            
            if children_data:
                self._add_nodes_to_tree(new_textual_node, children_data)

    def create_tree(self, field_id, field):
        yield Label(field["label"])
        
        root_label = field.get("root_label", "Root")
        root_data = field.get("root_data", None)
        
        tree_widget = Tree(label=root_label, data=root_data, id=field_id)
        
        # Set Tree-specific attributes
        tree_widget.show_root = field.get("show_root", True)
        tree_widget.show_guides = field.get("show_guides", True)
        tree_widget.guide_depth = field.get("guide_depth", 4)
        tree_widget.auto_expand = field.get("auto_expand", True) # Note: auto_expand on Tree itself, not individual nodes here
        tree_widget.disabled = field.get("disabled", False)
        
        nodes_data = field.get("nodes", [])
        self._add_nodes_to_tree(tree_widget.root, nodes_data)
        
        yield tree_widget

    def create_datatable(self, field_id, field):
        yield Label(field["label"])
        
        table = DataTable(id=field_id)
        
        # Set DataTable-specific attributes
        table.cursor_type = field.get("cursor_type", "row")
        table.show_cursor = field.get("show_cursor", True)
        table.zebra_stripes = field.get("zebra_stripes", False)
        table.fixed_rows = field.get("fixed_rows", 0)
        table.fixed_columns = field.get("fixed_columns", 0)
        table.disabled = field.get("disabled", False)
        
        columns_data = field.get("columns", [])
        if not columns_data:
            raise ValueError(f"DataTable '{field_id}' requires 'columns' to be defined.")
        table.add_columns(*columns_data)
        
        rows_data = field.get("rows", [])
        row_keys_data = field.get("row_keys", None)
        
        if row_keys_data and len(row_keys_data) != len(rows_data):
            raise ValueError(
                f"For DataTable '{field_id}', the length of 'row_keys' ({len(row_keys_data)}) "
                f"must match the length of 'rows' ({len(rows_data)})."
            )
            
        for i, row_content in enumerate(rows_data):
            key = row_keys_data[i] if row_keys_data else None
            if not isinstance(row_content, (list, tuple)):
                raise ValueError(
                    f"Each item in 'rows' for DataTable '{field_id}' must be a list or tuple. "
                    f"Found: {row_content}"
                )
            table.add_row(*row_content, key=key)
            
        yield table

    def create_listview(self, field_id, field):
        yield Label(field["label"])
        
        items_data = field.get("items", [])
        list_item_widgets = []
        for item_string in items_data:
            if not isinstance(item_string, str):
                raise ValueError(
                    f"Each item in 'items' for ListView '{field_id}' must be a string. "
                    f"Found: {item_string}"
                )
            list_item_widgets.append(ListItem(Label(item_string)))
            
        list_view = ListView(*list_item_widgets, id=field_id)
        
        initial_index = field.get("initial_index", None)
        if initial_index is not None:
            # Ensure index is valid if list is not empty
            if list_item_widgets and 0 <= initial_index < len(list_item_widgets):
                 list_view.index = initial_index
            elif initial_index != 0: # Allow initial_index 0 for empty list (noop)
                 # Or raise error, or log warning. For now, let Textual handle out-of-bounds.
                 # Textual might clamp it or error later if invalid.
                 # Explicitly setting to an invalid index can cause issues.
                 # We'll rely on Textual's default behavior or erroring if index is problematic.
                 pass


        list_view.disabled = field.get("disabled", False)
        
        yield list_view
