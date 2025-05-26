# **Textual Library Widgets for Information Collection: A Technical Guide for Formulator App Enhancement**

## **1\. Introduction**

### **Purpose**

This report serves as a definitive technical guide to the Textual library's built-in widgets and elements specifically designed for information collection within Terminal User Interfaces (TUIs). It aims to provide developers of the "Formulator app" with the necessary detailed information—including widget types, specific attributes, event handling, and styling options—to accurately update and enhance their YAML-based form specification capabilities. The Textual framework itself is a Rapid Application Development (RAD) environment for Python, enabling the construction of sophisticated user interfaces that can operate both in the terminal and, increasingly, in web browsers.1 This foundation underscores the importance of a comprehensive widget inventory for any application aiming to simplify or abstract Textual UI development. The focus herein is on current, core Textual library components, ensuring relevance and compatibility.

### **Scope Clarification**

The report will meticulously detail widgets directly involved in user input, selection, and data capture. Widgets primarily intended for static display (e.g., Static, Label, Markdown unless used interactively for selection) or layout purposes are excluded unless they possess interactive features pertinent to information collection. External or third-party widget libraries, such as the experimental textual-inputs package 2, fall outside the scope of this document, which concentrates exclusively on the official Textual framework's offerings. Textual boasts a rich library of widgets, providing a comprehensive set of components such as buttons, inputs, checkboxes, and more, allowing for the efficient building of interactive interfaces.3

### **Navigating the Report**

Each family of information-collecting widgets is presented in its own dedicated section. This is followed by a discussion of common attributes and overarching styling principles applicable across multiple widget types. For quick reference and ease of integration into the Formulator app, key tables summarizing attributes, events, and styling classes are provided for the most pertinent widgets. This structured approach is intended to facilitate the mapping of Textual's capabilities to the Formulator's YAML schema, thereby exposing the full potential of Textual for form creation.

## **2\. Core Text-Based Input Widgets**

The ability for users to enter textual data is a cornerstone of most form-based applications. Whether it's a name, an address, a detailed description, or a password, text input fields are ubiquitous. Textual provides a robust set of widgets designed to handle various text input scenarios, from simple single-line entries to complex multi-line documents with syntax highlighting, and even structured input through masking. The quality, flexibility, and feature set of these text input widgets significantly influence both the user experience and the integrity of the collected data. Textual's provision of Input, TextArea, and the more recent MaskedInput demonstrates a commitment to addressing diverse text input requirements comprehensively. For the Formulator app, these widgets will likely constitute some of the most frequently utilized components in YAML form definitions, making a thorough understanding and exposure of their full range of attributes critically important.

### **2.1. Input Widget**

The Input widget is a versatile single-line text input control, serving as a fundamental building block for capturing simple textual data within Textual applications.4 It is designed to be focusable and acts as a container for the text entered by the user.

Key Attributes for Information Collection:  
The Input widget offers a rich set of attributes to control its behavior and appearance, crucial for form development 5:

* value (str): Represents the current text content within the input field. This is essential for retrieving the data entered by the user. Defaults to "".  
* placeholder (str): Provides hint text displayed within the input field when it is empty, guiding the user on the expected input. Defaults to "".  
* password (bool): When set to True, this attribute obfuscates the input (e.g., with asterisks or bullets), making it suitable for sensitive data like passwords. Defaults to False.  
* restrict (str): Accepts a regular expression string that limits the characters a user can enter. The widget prevents the addition of characters that would cause the full value to no longer match the regex. This is useful for enforcing specific formats, such as numeric-only IDs or alphanumeric codes. Defaults to None. The restrict regular expression is applied to the full value, not just the new character, and is checked on all edit operations, not just insertions.5  
* type (str): Can be set to "text", "integer", or "number" to enforce basic data types. This setting prevents users from typing invalid characters and automatically applies appropriate built-in validators. For instance, "integer" restricts input to whole numbers, and "number" to floating-point numbers.5 Defaults to "text".  
* max\_length (int): Defines the maximum number of characters that can be entered into the input field. If set to a value greater than 0, it prevents further character entry once the limit is reached. Defaults to 0 (no maximum length).  
* validators (Validator | Iterable\[Validator\]): Allows for the attachment of one or more custom validator functions or classes. These are checked when the value changes, the input is submitted, or focus moves out of the input, providing a powerful mechanism for complex business rule enforcement. Defaults to None.  
* validate\_on (Iterable\[str\]): Determines when validation occurs. It accepts an iterable of strings, which can include "blur" (when focus is lost), "changed" (when the value changes), and "submitted" (when Enter is pressed). By default, validation occurs for all these messages, offering fine-grained control over user feedback.  
* valid\_empty (bool): If True, allows empty values to bypass validators and be considered valid. This is important for optional fields in a form. Defaults to False.  
* disabled (bool): When True, the input field is non-interactive and typically styled to indicate its disabled state. Defaults to False.  
* compact (bool): Introduced more broadly across widgets 7, this attribute, when True, renders the Input widget with a compact style, typically without borders. This is useful for creating denser user interfaces. Defaults to False.5  
* suggester (Suggester | None): Associates a suggester instance for auto-completion capabilities. Defaults to None.  
* select\_on\_focus (bool): If True, all text within the input is selected when the widget gains focus. Defaults to True.  
* Common attributes like name (str | None), id (str | None), classes (str | None), and tooltip (RenderableType | None) are also available for identification, styling, and providing help text.

Recent changes to the Input widget include the removal of view\_position and cursor\_position as reactive attributes (with cursor\_position now being a property that proxies to the Input.selection reactive attribute).6 Furthermore, input validation for floats and integers now accepts embedded underscores (e.g., "1\_234\_567" is considered valid), enhancing usability for numeric inputs.6

Key Events/Messages:  
The Input widget emits messages to signal user interactions or state changes 5:

* Input.Changed: This message is posted whenever the value of the input field changes. It includes the input widget itself, the new value, and the validation\_result (if validators are present). This event is crucial for implementing real-time feedback or dynamic form behaviors.  
* Input.Submitted: This message is posted when the user presses the Enter key within the input field. Similar to Changed, it includes the input, value, and validation\_result. This event is typically used to trigger form submission for that field or to move to the next field.

Component CSS Classes for Styling:  
For fine-grained visual customization, the Input widget exposes several component classes that can be targeted with Textual CSS 5:

* input--cursor: Styles the cursor within the input field.  
* input--placeholder: Styles the placeholder text when it is visible.  
* input--suggestion: Styles the auto-completion suggestion text.  
* input--selection: Styles the currently selected text within the input. Additionally, Textual applies a default style for the \-invalid CSS class (often a red border), which is automatically added to the Input widget when its validation fails. Conversely, a \-valid class can be styled (e.g., with a green border) to indicate successful validation.

Use Cases:  
The Input widget is suitable for a wide range of form fields, including names, email addresses, search queries, passwords, simple numeric inputs (age, quantity), and any other single-line textual data.  
**Table: Input Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| value | str | "" | The current text content. Core for data retrieval. |
| placeholder | str | "" | Hint text for empty input. Improves UX. |
| password | bool | False | Obfuscates input for sensitive data (e.g., passwords). |
| restrict | str (regex) | None | Limits allowed characters based on a regular expression. Enforces specific formats. |
| type | str | "text" | "text", "integer", "number". Enforces basic data types and applies built-in validation. |
| max\_length | int | 0 | Maximum number of characters allowed. |
| validators | \`Validator \\ | Iterable\[Validator\]\` | None |
| validate\_on | Iterable\[str\] | ("blur", "changed", "submitted") | When to perform validation ("blur", "changed", "submitted"). |
| valid\_empty | bool | False | If True, empty input is considered valid, bypassing validators. For optional fields. |
| disabled | bool | False | Disables user interaction. |
| compact | bool | False | Enables borderless style, useful for dense UIs. |
| suggester | \`Suggester \\ | None\` | None |
| select\_on\_focus | bool | True | Selects all text on focus. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

### **2.2. TextArea Widget**

For scenarios requiring multi-line text input, such as detailed descriptions, comments, or even code snippets, Textual provides the TextArea widget.4 It supports features like syntax highlighting, soft wrapping, and line numbers, making it a powerful tool for richer text editing experiences.

Key Attributes for Information Collection:  
The TextArea widget comes with several attributes to manage its content and behavior 8:

* text (str): Holds the initial and current multi-line text content of the area. Defaults to "".  
* language (str | None): Specifies the programming or markup language for syntax highlighting (e.g., "python", "markdown", "json"). Highlighting is active if a language is set. Defaults to None.  
* theme (str): Determines the syntax highlighting theme to be used. Textual includes a set of built-in themes and allows for custom themes. The default is 'css'.8 Textual has introduced a new theme system, and tree-sitter languages for syntax highlighting are now loaded lazily to improve cold-start time.6  
* soft\_wrap (bool): If True, lines that exceed the widget's width will wrap to the next line visually without inserting newline characters. Defaults to True.  
* read\_only (bool): When True, users are prevented from modifying the content via keyboard input, though programmatic changes are still possible. Defaults to False.  
* show\_line\_numbers (bool): Toggles the visibility of a line number gutter on the left edge of the widget. Defaults to False.  
* selection (Selection): A reactive attribute representing the current text selection, including the cursor's position. The selected text can be accessed via the TextArea.selected\_text property.  
* disabled (bool): If True, the entire widget is disabled and non-interactive. Defaults to False.  
* compact (bool): When True, enables a compact, borderless style for the TextArea.7 Defaults to False.  
* tab\_behavior (Literal\['focus', 'indent'\]): Controls the behavior of the Tab key. If 'focus', Tab moves focus to the next widget; if 'indent', Tab inserts an indentation. Defaults to 'focus'.  
* indent\_width (int): Specifies the number of spaces used for indentation when tab\_behavior is 'indent' or when auto-indenting. Defaults to 4\.  
* Common attributes like name (str | None), id (str | None), classes (str | None), and tooltip (RenderableType | None) are also available.

Key Events/Messages:  
The TextArea emits messages to notify of changes 8:

* TextArea.Changed: Posted when the text content of the TextArea is modified.  
* TextArea.SelectionChanged: Posted when the text selection (including cursor movement) changes.

Component CSS Classes for Styling:  
The TextArea offers component classes for detailed styling, although styles defined in the chosen TextAreaTheme take precedence for syntax highlighting 8:

* text-area--cursor: Styles the cursor.  
* text-area--gutter: Styles the line number gutter.  
* text-area--cursor-line: Styles the entire line where the cursor is currently located.  
* text-area--selection: Styles the highlighted text selection.  
* text-area--matching-bracket: Styles matching brackets when match\_cursor\_bracket is enabled.

Use Cases:  
Ideal for inputting longer pieces of text such as user comments, detailed descriptions, notes, articles, or even small blocks of code or configuration data within a form.  
**Table: TextArea Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| text | str | "" | The multi-line text content. Core for data retrieval. |
| language | \`str \\ | None\` | None |
| theme | str | "css" | Syntax highlighting theme. |
| soft\_wrap | bool | True | Enables visual text wrapping. |
| read\_only | bool | False | Prevents user modification via keyboard. |
| show\_line\_numbers | bool | False | Toggles visibility of line numbers. |
| selection | Selection | N/A | Represents the current text selection and cursor position. |
| disabled | bool | False | Disables user interaction. |
| compact | bool | False | Enables borderless style. |
| tab\_behavior | Literal\['focus', 'indent'\] | 'focus' | Controls Tab key behavior: focus change or indentation. |
| indent\_width | int | 4 | Number of spaces for indentation. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

### **2.3. MaskedInput Widget**

Introduced in Textual version 0.80.0, the MaskedInput widget is a specialization of the Input widget designed to restrict user input according to a predefined template mask.6 This is particularly useful for fields that require a fixed format, such as phone numbers, dates, or serial keys, as it guides user input and can implicitly validate the format. The addition of such a widget signifies a move towards providing components that enforce data structure directly at the point of entry, potentially reducing the need for complex client-side validation logic for common structured formats and improving the user experience by preventing many types of invalid input from the outset.

Key Attributes for Information Collection:  
The MaskedInput widget inherits many attributes from Input but introduces its own crucial template attribute 9:

* template (str): This is the core attribute that defines the input mask. The template string's length determines the maximum input length. Special characters in the mask define the type of character allowed at each position (e.g., A for \[A-Za-z\], 9 for \[0-9\]) and whether it's required or optional. Other characters act as separators. Case conversion characters (\>, \<, \!) and placeholder termination (;c) are also supported. This attribute is required.  
* value (str | None): The current input value, which will conform to the mask. Defaults to None.  
* placeholder (str): Optional placeholder text. The mask itself can also define a placeholder character. Defaults to "".  
* validators (Validator | Iterable\[Validator\] | None): Inherited from Input. Can be used for validation beyond the mask's structural enforcement. Defaults to None.  
* validate\_on (Iterable\[InputValidationOn\] | None): Inherited from Input. Determines when validation occurs. Defaults to None (validates on blur, changed, submitted).  
* valid\_empty (bool): Inherited from Input. If True, an empty input is considered valid. Defaults to False.  
* disabled (bool): Disables the widget. Defaults to False.  
* Common attributes like name (str | None), id (str | None), classes (str | None), and tooltip (RenderableType | None) are available.  
* The compact attribute, while not explicitly listed for MaskedInput in its initial documentation 9, was added to the base Input widget later.7 Given that MaskedInput derives from Input, it is likely to inherit this attribute or have it added subsequently. This should be verified with the latest Textual version if a compact MaskedInput is required.

Key Events/Messages:  
As a derivative of Input, MaskedInput emits similar messages 9:

* MaskedInput.Changed: Posted when the value of the masked input changes.  
* MaskedInput.Submitted: Posted when the Enter key is pressed within the masked input.

Component CSS Classes for Styling:  
The MaskedInput widget inherits the input--\* component classes from the Input widget for styling its cursor, placeholder, suggestions, and selection.9 It also benefits from the automatic application of \-invalid and \-valid classes based on validation status.  
Use Cases:  
Excellent for inputs with a strict, predefined format such as phone numbers (e.g., (999) 999-9999), dates (e.g., 99/99/9999), postal codes, credit card numbers (with appropriate security considerations), or license keys.  
**Table: MaskedInput Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| template | str | "" (Required) | The mask string defining allowed characters, separators, and format. Core for structured input. |
| value | \`str \\ | None\` | None |
| placeholder | str | "" | Optional placeholder text; mask can also define placeholder. |
| validators | \`Validator \\ | Iterable\[Validator\] \\ | None\` |
| validate\_on | \`Iterable\[InputValidationOn\] \\ | None\` | None |
| valid\_empty | bool | False | If True, empty input is valid. |
| disabled | bool | False | Disables user interaction. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

## **3\. Selection & Choice Widgets**

Forms frequently require users to make selections from a predefined set of options. This can range from simple binary choices (yes/no) to selecting one item from a long list, or multiple items from a set of preferences. Textual provides a diverse array of widgets to cater to these varied selection mechanisms, each suited to different data cardinalities and presentation styles. The availability of Checkbox, RadioSet (with RadioButton), Select, OptionList, and SelectionList demonstrates Textual's comprehensive approach to handling choice-based input. For the Formulator app, it is crucial to clearly differentiate these widgets within its YAML schema, enabling users to choose the most semantically appropriate widget for each form field based on the nature of the choice being presented.

### **3.1. Checkbox Widget**

The Checkbox widget is a standard UI element for representing a binary choice, typically indicating agreement, selection of an option, or toggling a boolean state.4 It visually shows a box that can be checked or unchecked by the user.

Key Attributes for Information Collection:  
Key attributes for the Checkbox widget include 10:

* value (bool): The core reactive attribute representing the current state of the checkbox. True indicates checked, and False indicates unchecked. Defaults to False.  
* label (ContentText): The text label displayed alongside the checkbox, describing its purpose (e.g., "I agree to the terms"). Defaults to "".  
* button\_first (bool): Determines the layout order. If True (the default), the checkbox visual element appears before the label; if False, it appears after.  
* disabled (bool): When True, the checkbox is non-interactive. Defaults to False.  
* compact (bool): If True, enables a compact, often borderless, style for the checkbox.7 Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).

Key Events/Messages:  
The primary event for a Checkbox is 10:

* Checkbox.Changed: This message is posted whenever the value (checked state) of the checkbox changes. The message includes the checkbox instance and its new value. This event is typically handled to react to the user's choice.

Component CSS Classes for Styling:  
Styling of the Checkbox can be achieved using these component classes 10:

* toggle--button: Targets the visual checkbox element itself.  
* toggle--label: Targets the text label associated with the checkbox.

Use Cases:  
Commonly used for agreeing to terms and conditions, toggling boolean settings (e.g., "Enable notifications"), or as part of a group where multiple independent options can be selected.  
**Table: Checkbox Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| value | bool | False | Current state (True for checked, False for unchecked). Core for data retrieval. |
| label | ContentText | "" | Text label describing the checkbox's purpose. |
| button\_first | bool | True | If True, checkbox appears before the label. |
| disabled | bool | False | Disables user interaction. |
| compact | bool | False | Enables a compact, borderless style. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

### **3.2. RadioButton & RadioSet Widgets**

For scenarios where a user must select only one option from a mutually exclusive list, Textual provides RadioButton and RadioSet widgets.4 An individual RadioButton represents a single choice, while the RadioSet acts as a container that groups multiple RadioButtons, enforcing the single-selection constraint.11

RadioButton Key Attributes:  
These attributes apply to individual radio buttons within a set 11:

* value (bool): Indicates its individual selection state (True if this button is the one selected within its RadioSet). Defaults to False.  
* label (ContentText): The descriptive text label for this specific radio button option. Defaults to "".  
* button\_first (bool): Determines if the radio button visual appears before or after its label. Defaults to True.  
* disabled (bool): Disables this specific radio button, preventing its selection. Defaults to False.  
* compact (bool): Enables a compact style for the individual radio button.7 Defaults to False.

RadioSet Key Attributes:  
These attributes apply to the container managing the group of radio buttons 12:

* buttons (Iterable): Defines the radio buttons that belong to this set. This can be an iterable of string labels (from which RadioButton instances will be created) or pre-constructed RadioButton instances.  
* pressed\_button (RadioButton | None): A read-only property that returns the currently selected RadioButton instance within the set, or None if no button is selected.  
* pressed\_index (int): A read-only property that returns the index of the currently selected RadioButton within the set, or \-1 if no button is selected. This is key for identifying the user's choice.  
* disabled (bool): When True, disables the entire RadioSet, preventing interaction with any of its buttons. Defaults to False.  
* compact (bool): Enables a compact style for the RadioSet container and its contents.7 Defaults to False.  
* Common attributes for the set: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).

**Key Events/Messages:**

* RadioButton.Changed 11: Posted when an individual RadioButton's state changes. This is less commonly handled directly if the buttons are part of a RadioSet, as the RadioSet.Changed event is usually more relevant for form logic.  
* RadioSet.Changed 12: This is the primary event for forms using RadioSet. It is posted when the selected button within the RadioSet changes. The message includes attributes like pressed (the RadioButton instance that was just pressed) and index (the index of the pressed button).

**Component CSS Classes for Styling:**

* For RadioButton 11:  
  * toggle--button: Targets the radio button visual element.  
  * toggle--label: Targets the text label of the radio button.  
* For RadioSet 12: No specific component classes are listed for the RadioSet container itself, but its layout (often within a Horizontal or Vertical container) and the styling of its contained RadioButtons can be controlled via CSS. RadioSet itself now has a default width of 1fr.7

Use Cases:  
Ideal for selecting a single option from a small, mutually exclusive list, such as gender, payment method, shipping option, or a rating.  
**Table: RadioSet Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| buttons | Iterable | N/A (Required) | Defines the radio button options in the set (labels or RadioButton instances). |
| pressed\_button | \`RadioButton \\ | None\` | (Read-only) |
| pressed\_index | int | (Read-only) | Index of the selected RadioButton. Key for retrieving choice. |
| disabled | bool | False | Disables the entire set. |
| compact | bool | False | Enables a compact style for the set. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

### **3.3. Select Widget**

The Select widget provides a compact, dropdown-style control that allows users to choose a single option from a predefined list.1 When not active, it displays the currently selected option or a prompt; when activated, it expands to show the list of available options.

Key Attributes for Information Collection:  
Key attributes for configuring the Select widget include 13:

* options (Iterable\]): This is a required attribute (unless allow\_blank is True) that defines the list of choices. Each item in the iterable is a tuple, where the first element is the display label (a string or Rich renderable) and the second element is the actual underlying value associated with that option.  
* prompt (str): The text displayed in the Select widget when no option is currently selected (and allow\_blank is True). Defaults to 'Select'.  
* allow\_blank (bool): If True, the widget can be in a state where no option is selected. In this case, its value will be the special constant Select.BLANK. Defaults to True. If False, an option must always be selected (the first option becomes selected by default if no initial value is provided).  
* value (Any): This reactive attribute holds the actual underlying value of the currently selected option. Its type depends on the values provided in the options list. If allow\_blank is True and no selection is made, its value is Select.BLANK.  
* disabled (bool): When True, the Select widget is non-interactive. Defaults to False.  
* compact (bool): If True, enables a compact, borderless style for the Select widget.7 Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).

Key Events/Messages:  
The primary event for the Select widget is 13:

* Select.Changed: This message is posted whenever the selected value of the widget changes. The message includes the select widget instance and its new value. This is crucial for reacting to user selections in a form.

Styling:  
The Select widget can be styled using general Textual CSS properties. Common properties to adjust include width and margin. No specific component classes for the Select widget itself are detailed in 13 beyond general widget styling capabilities.  
Use Cases:  
Suitable for selecting a single option from a list, especially when screen space is a concern or the list of options is moderately long. Examples include selecting a country, state, status, category, or any predefined enumerated value.  
**Table: Select Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| options | Iterable\] | N/A (Required unless allow\_blank=True) | List of (display\_label, actual\_value) tuples. Defines choices. |
| prompt | str | "Select" | Text displayed when no option is selected (if allow\_blank=True). |
| allow\_blank | bool | True | If True, allows no selection (value becomes Select.BLANK). |
| value | Any | (first option or Select.BLANK) | The actual value of the selected option. Core for data retrieval. |
| disabled | bool | False | Disables user interaction. |
| compact | bool | False | Enables a compact, borderless style. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

### **3.4. OptionList Widget**

The OptionList widget displays a vertical, scrollable list of options from which a user can highlight and select a single item.4 Options can be simple strings or more complex Rich renderables. It is primarily designed for selection, rather than for complex data entry within the list items themselves.

Key Attributes for Information Collection:  
Important attributes for the OptionList include 14:

* options (Sequence): Defines the options to be displayed in the list. The exact structure of OptionType can vary; often, it's a sequence of strings (labels) or tuples like (label, id\_or\_value). A None value in the sequence can be used to specify a separator, as the Separator object is no longer supported for this purpose.6  
* highlighted (int | None): A reactive attribute representing the index of the currently highlighted option. If no option is highlighted, its value is None.  
* disabled (bool): When True, the entire OptionList is non-interactive. Defaults to False.  
* compact (bool): If True, enables a compact display style for the OptionList.7 Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).

Key Events/Messages:  
The OptionList emits messages related to highlighting and selection 14:

* OptionList.OptionHighlighted: This message is sent when a new option in the list becomes highlighted (e.g., via arrow key navigation). It includes the option\_list instance and the index of the highlighted option.  
* OptionList.OptionSelected: This message is sent when an option is actively selected (e.g., by pressing Enter on the highlighted option). It includes the option\_list, index, the selected option itself, and its option\_id (if available). This is the key event for capturing the user's choice in a form.

Component CSS Classes for Styling:  
The OptionList provides several component classes for detailed styling 14:

* option-list--option: Styles options that are not disabled, highlighted, or hovered.  
* option-list--option-disabled: Styles disabled options.  
* option-list--option-highlighted: Styles the currently highlighted option.  
* option-list--option-hover: Styles an option when the mouse cursor is over it.  
* option-list--separator: Styles the separator lines between options.

Use Cases:  
Used for selecting a single item from a visible list of choices. This can be suitable for navigation menus that result in a selection, or for choosing from a set of commands or items where the options are best presented as an explicit list.  
**Table: OptionList Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| options | Sequence | () | Sequence of options (labels, (label, value) tuples, or Rich renderables) and None for separators. |
| highlighted | \`int \\ | None\` | None |
| disabled | bool | False | Disables the entire list. |
| compact | bool | False | Enables a compact display style. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

### **3.5. SelectionList Widget**

When the requirement is to allow users to select multiple options from a list, the SelectionList widget is the appropriate choice.4 It displays a vertical list of items, each of which can be individually toggled to a selected or deselected state.

Key Attributes for Information Collection:  
Key attributes for the SelectionList are 15:

* \*selections (Selection | tuple): This parameter defines the content of the selection list. It can accept Selection objects (which allow specifying a prompt, a unique value, initial selected state, ID, and enabled state) or tuples. Tuples typically contain (prompt, value) and can optionally include a boolean for the initial selected state.  
* selected (list\[Any\]): A read-only property that returns a list of the actual underlying values of all items currently in the selected state. This is the primary attribute for retrieving the collected data from the widget.  
* highlighted (int | None): A reactive attribute indicating the index of the currently highlighted selection in the list. None if nothing is highlighted.  
* disabled (bool): When True, the entire SelectionList is non-interactive. Defaults to False.  
* compact (bool): If True, enables a compact style for the SelectionList.7 Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).

Key Events/Messages:  
The SelectionList emits several messages to signal changes in selection or highlighting 15:

* SelectionList.SelectedChanged: This is a crucial event for forms. It is sent whenever the collection of selected values changes (i.e., an item is selected or deselected). For bulk changes (e.g., select\_all), only a single SelectedChanged message is sent.  
* SelectionList.SelectionToggled: Sent when an individual selection's state is explicitly toggled (e.g., by user interaction or a toggle method call). A message is sent for each option toggled.  
* SelectionList.SelectionHighlighted: Sent when a selection in the list is highlighted through navigation.

Component CSS Classes for Styling:  
The SelectionList provides specific component classes for styling its elements, and it also inherits classes from OptionList 15:

* selection-list--button: Styles the default button appearance within each selection item.  
* selection-list--button-selected: Styles a button when its corresponding item is selected.  
* selection-list--button-highlighted: Styles a button when its item is highlighted.  
* selection-list--button-selected-highlighted: Styles a button that is both selected and highlighted.  
* Inherited from OptionList: option-list--option, option-list--option-disabled, option-list--option-highlighted, option-list--option-hover, option-list--separator.

Use Cases:  
Ideal for scenarios where users need to select multiple items from a list, such as choosing multiple preferences, applying tags, selecting features, or any multi-select checklist functionality.  
**Table: SelectionList Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| \*selections | \`Selection \\ | tuple\` | N/A (Required) |
| selected | list\[Any\] | (Read-only) | List of values of the currently selected items. Core for data retrieval. |
| highlighted | \`int \\ | None\` | None |
| disabled | bool | False | Disables the entire list. |
| compact | bool | False | Enables a compact style. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

## **4\. Toggle Widgets**

Toggle widgets are used to represent a binary state, typically "on" or "off," "enabled" or "disabled." While the term "ToggleButton" is a common UI concept 16, within the Textual library's user-facing widget set, the primary component for a distinct on/off toggle is the Switch widget.4 The ToggleButton name appears more as a base or internal component that widgets like Checkbox and RadioButton build upon, as evidenced by event parameters in their documentation referring to a toggle\_button of type ToggleButton.10 For direct use in forms to collect a boolean state via a visual toggle, Switch is the designated widget. This distinction is important for the Formulator app to ensure it exposes the correct widget to its users for this purpose.

### **4.1. Switch Widget**

The Switch widget provides a classic on/off toggle, visually resembling a physical switch, and is used to represent and collect a boolean value.3

Key Attributes for Information Collection:  
The Switch widget's behavior is controlled by these attributes 19:

* value (bool): The core reactive attribute representing the current state of the switch. True signifies the "on" state, and False signifies the "off" state. Defaults to False.  
* animate (bool): If True, the switch will visually animate when its state is toggled from on to off or vice-versa. Defaults to True.  
* disabled (bool): When True, the switch is non-interactive and cannot be toggled by the user. Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).  
* The compact attribute, which provides a borderless style, is not explicitly listed for the Switch widget in the primary documentation snippets 19 in the same way it is for many other input widgets that received it in a batch update.7 If a borderless switch is desired, custom CSS might be necessary, or this should be verified against the very latest Textual documentation, as widget features evolve.

Key Events/Messages:  
The main event emitted by the Switch widget is 19:

* Switch.Changed: This message is posted whenever the value (on/off state) of the switch changes. The message includes the switch instance and its new value. This event allows the application to react to the user toggling the switch.

Component CSS Classes for Styling:  
For custom styling, the Switch widget provides a specific component class 19:

* switch--slider: Targets the moving part (the "slider" or "thumb") of the switch, allowing its appearance to be customized independently of the switch's background.

Use Cases:  
Commonly used for toggling application settings, enabling or disabling features, or any scenario where a clear binary on/off choice needs to be presented to the user.  
**Table: Switch Widget \- Key Attributes**

| Attribute | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| value | bool | False | Current state (True for on, False for off). Core for data retrieval. |
| animate | bool | True | If True, the switch animates when toggled. |
| disabled | bool | False | Disables user interaction. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

## **5\. Hierarchical & List-Based Selection Widgets**

Beyond simple lists of options, forms sometimes require users to select items from more complex or structured datasets. This can involve navigating hierarchical data, such as a file system or a multi-level category tree, or selecting from lists where each item might itself be a complex, custom-rendered component. Textual provides several widgets—ListView (with ListItem), DirectoryTree, and Tree—to cater to these more advanced selection scenarios. The ListItem widget, while not an input widget in itself, plays a crucial role as it can host other widgets 21, potentially allowing for the creation of lists containing complex, selectable sub-components. However, the primary interaction model for ListView remains the selection of the ListItem itself. For the Formulator app, representing these complex data sources and their corresponding selection mechanisms in YAML will require careful consideration, possibly involving ways to define tree structures or templates for custom list items.

### **5.1. ListView & ListItem Widgets**

The ListView widget is designed to display a scrollable vertical list of ListItem objects. It supports keyboard navigation for highlighting and selecting a single item from the list.4 The ListItem serves as an individual, focusable entry within the ListView and, importantly, can contain other child widgets, allowing for rich and custom item rendering.20

ListView Key Attributes:  
Attributes for configuring the ListView include 22:

* initial\_index (int | None): Specifies the index of the ListItem that should be highlighted when the ListView is first mounted. Defaults to 0 (the first item).  
* index (int): A reactive attribute representing the index of the currently highlighted ListItem. Defaults to 0\.  
* disabled (bool): When True, the entire ListView is non-interactive. Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).

ListItem Key Attributes:  
Attributes for individual ListItems include 21:

* \*children (Widget): Allows ListItem to contain one or more child widgets, enabling complex item layouts.  
* highlighted (bool): A reactive attribute that is True if the ListItem is currently highlighted within its ListView. Defaults to False.  
* disabled (bool): When True, this specific ListItem may be styled differently or behave as non-selectable, though ListView's overall disabled state takes precedence. Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None).

Key Events/Messages (ListView):  
The ListView emits messages to signal highlighting and selection events 22:

* ListView.Highlighted: Posted when the highlighted item changes (e.g., due to arrow key navigation). The message includes the list\_view instance and the item (the ListItem that is now highlighted).  
* ListView.Selected: Posted when a ListItem is actively selected (e.g., by pressing Enter). The message includes the list\_view instance and the selected item. The "value" collected in a form context would typically be an identifier or data associated with this selected ListItem.

Styling:  
Both ListView (as a VerticalScroll derivative) and its ListItem children can be styled using Textual CSS. Common properties like width, height, padding, and border can be applied.  
Use Cases for Forms:  
ListView is suitable for selecting a single item from a list where each item might require custom rendering (e.g., an icon plus text, multiple pieces of information per item). The information collected is typically an identifier associated with the chosen ListItem, or data retrieved from the ListItem or its children upon selection. While ListItem can host input widgets, the ListView's core interaction model is selection of the ListItem itself, not direct data entry into hosted widgets as part of the ListView's selection mechanism.  
**Table: ListView \- Key Attributes & Events**

| Element | Attribute/Event | Type | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| ListView | initial\_index | \`int \\ | None\` |
| ListView | index | int | Currently highlighted index (reactive). |
| ListView | disabled | bool | Disables the entire list. |
| ListView | ListView.Highlighted | Event | Posted when an item is highlighted. item attribute gives the ListItem. |
| ListView | ListView.Selected | Event | Posted when an item is selected. item attribute gives the selected ListItem. Key for form data. |
| ListItem | \*children | Widget | Child widgets hosted by the ListItem. Allows custom item rendering. |
| ListItem | highlighted | bool | True if currently highlighted (reactive). |

### **5.2. DirectoryTree Widget**

The DirectoryTree widget provides a specialized tree control for navigating and selecting files or directories from the local filesystem.4 This is invaluable for form fields that require file paths or directory locations as input.

Key Attributes for Information Collection:  
Key attributes for the DirectoryTree widget include 23:

* path (str | Path): The root directory path that the tree should display and allow navigation within. This is a required parameter for initialization.  
* show\_root (bool): If True, the root node of the directory tree (representing the initial path) will be displayed. Defaults to True.  
* disabled (bool): When True, the DirectoryTree is non-interactive. Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).  
* Inherited tree attributes like show\_guides (bool, default True) and guide\_depth (int, default 4\) also affect appearance.

Key Events/Messages:  
The DirectoryTree emits specific messages when files or directories are selected 23:

* DirectoryTree.FileSelected: Posted when a file node in the tree is selected by the user. The message includes the node (the TreeNode for the file) and, crucially for forms, the path (a Path object) of the selected file.  
* DirectoryTree.DirectorySelected: Posted when a directory node in the tree is selected. Similarly, it includes the node and the path of the selected directory.

Component CSS Classes for Styling:  
The DirectoryTree offers component classes for styling different elements within the tree view 23:

* directory-tree--extension: Targets the file name extension part of file labels.  
* directory-tree--file: Targets file labels.  
* directory-tree--folder: Targets folder labels.  
* directory-tree--hidden: Targets hidden files or directories.  
* It also inherits styling capabilities from the base Tree widget.

Use Cases:  
Primarily used for "file input" fields in forms, allowing users to browse and select a file for upload, processing, or reference. Also used for selecting a directory for operations like saving files or setting a working folder.  
**Table: DirectoryTree \- Key Attributes & Events**

| Attribute/Event | Type | Description & Form Relevance |
| :---- | :---- | :---- |
| path | \`str \\ | Path\` |
| show\_root | bool | If True, displays the root node. |
| disabled | bool | Disables the tree. |
| DirectoryTree.FileSelected | Event | Posted when a file is selected. path attribute gives the Path to the file. Core for form data. |
| DirectoryTree.DirectorySelected | Event | Posted when a directory is selected. path attribute gives the Path to the directory. Core for form data. |
| name | \`str \\ | None\` |
| id | \`str \\ | None\` |
| classes | \`str \\ | None\` |
| tooltip | \`RenderableType \\ | None\` |

### **5.3. Tree Widget**

The Tree widget is a general-purpose control for displaying and navigating hierarchical data structures.3 Unlike DirectoryTree, it is not tied to the filesystem and can be populated with arbitrary nested data, making it suitable for a wide range of hierarchical selection tasks.

Key Attributes for Information Collection:  
Attributes relevant for using the Tree widget in forms include 24:

* label (TextType): The label for the root node of the tree. Required on initialization.  
* data (Any): Optional arbitrary data associated with the root node. Each TreeNode within the tree can also have its own associated data.  
* cursor\_node (TreeNode | None): A read-only property that returns the currently selected TreeNode instance, or None if no node is selected. The data or label of this node can be the value collected by the form.  
* show\_root (bool): If True, the root node of the tree is displayed. Defaults to True.  
* disabled (bool): When True, the Tree widget is non-interactive. Defaults to False.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).  
* Appearance attributes: show\_guides (bool, default True), guide\_depth (int, default 4), auto\_expand (bool, default True).

Key Events/Messages:  
The Tree widget emits messages for various node interactions 24:

* Tree.NodeSelected: This is the most important event for form data collection. It is posted when a node in the tree is selected by the user. The message includes the node (the selected TreeNode instance), from which its label, data, or other properties can be extracted as the form value.  
* Tree.NodeExpanded, Tree.NodeCollapsed: Posted when a node is expanded or collapsed, respectively.  
* Tree.NodeHighlighted: Posted when a node is highlighted through navigation.

Component CSS Classes for Styling:  
For visual customization, the Tree widget provides these component classes 24:

* tree--cursor: Styles the cursor indicating the selected/active line.  
* tree--guides: Styles the indentation guide lines.  
* tree--label: Styles the text labels of the tree items.  
* tree--highlight: Styles highlighted items (often the line under the cursor or selected node).

Use Cases:  
Suitable for selecting items from any custom-defined hierarchical structure, such as product categories, organizational charts, nested configuration options, or any scenario where data is naturally represented as a tree and a single item needs to be chosen.  
**Table: Tree Widget \- Key Attributes & Events**

| Attribute/Event | Type | Description & Form Relevance |
| :---- | :---- | :---- |
| label | TextType | (Required on init) Label of the root node. |
| data | Any | (Optional on init) Data associated with the root node. Each node can have data. |
| cursor\_node | \`TreeNode \\ | None\` |
| show\_root | bool | If True, displays the root node. |
| disabled | bool | Disables the tree. |
| Tree.NodeSelected | Event | Posted when a node is selected. node attribute gives the TreeNode. Core for form data. |
| name | \`str \\ | None\` |
| id | \`str \\ | None\` |
| classes | \`str \\ | None\` |
| tooltip | \`RenderableType \\ | None\` |

## **6\. Action Widgets for Forms**

Forms are not just about collecting data; they also require mechanisms for users to submit that data, cancel the operation, or trigger other related actions. Buttons are the primary interactive elements for these purposes. Textual's Button widget is well-suited for these roles, offering semantic variants and event handling that integrate cleanly into form workflows. For the Formulator app, allowing easy definition of buttons—including their labels, visual styles (variants), and the actions they trigger—is essential for creating fully functional forms.

### **6.1. Button Widget**

The Button widget is a standard clickable button that users can interact with via mouse clicks or by pressing Enter when the button has focus.1 It is a fundamental component for triggering actions within an application.

Key Attributes for Form Actions:  
Attributes that are particularly relevant for using buttons in forms include 25:

* label (str): The text displayed on the button, clearly indicating its action (e.g., "Submit", "Save", "Cancel", "Next"). Defaults to "".  
* variant (str): Controls the semantic styling and appearance of the button. Available variants are "default", "primary", "success", "warning", and "error". The "primary" variant is often used for the main submission action of a form. Defaults to "default".  
* disabled (bool): When True, the button is non-interactive and visually styled to indicate its disabled state. This is useful for preventing form submission until validation passes or certain conditions are met. Defaults to False.  
* compact (bool): If True, enables a compact, borderless style for the button.7 This can be useful for toolbars or denser form layouts. Defaults to False.  
* action (str | None): An optional action string. If provided, Textual will attempt to automatically dispatch this action when the button is pressed. If an action is specified, the Button.Pressed message will not be sent. Defaults to None.  
* Common attributes: name (str | None), id (str | None), classes (str | None), tooltip (RenderableType | None).

A notable change is that Button widgets now use Textual markup for their labels rather than console markup, allowing for richer text styling within the button itself.6

Key Events/Messages:  
The primary event for reacting to button presses in form logic is 25:

* Button.Pressed: This message is sent when the button is pressed by the user, provided that no action string was supplied to the button's constructor. This event is typically handled to trigger form submission, data validation, navigation, or other custom logic. The message includes a button attribute, which is the instance of the Button that was pressed.

Styling:  
The variant attribute provides a set of predefined styles. Buttons can be further customized using Textual CSS by targeting their id, classes, or the Button type itself. While no specific component classes for Button are listed in 25, general widget styling properties like width, height, margin, padding, border, background, and color can be applied. The default styling for a Button includes borders and a min-width, which contribute to spacing around the label; these can be overridden with CSS (e.g., border: none;).25  
Use Cases:  
Essential for form actions such as:

* Submitting form data.  
* Resetting form fields to their initial values.  
* Canceling the form operation and closing the form.  
* Navigating between steps in a multi-page form.  
* Triggering any other custom action related to the form's data or state.

**Table: Button Widget \- Key Attributes & Events**

| Attribute/Event | Type | Default | Description & Form Relevance |
| :---- | :---- | :---- | :---- |
| label | str | "" | Text displayed on the button (e.g., "Submit", "Cancel"). |
| variant | str | "default" | Semantic style: "default", "primary", "success", "warning", "error". |
| disabled | bool | False | Disables button interaction. Useful for form validation states. |
| compact | bool | False | Enables a compact, borderless style. |
| action | \`str \\ | None\` | None |
| Button.Pressed | Event | N/A | Sent when button is pressed (if no action). Key for triggering form logic. |
| name | \`str \\ | None\` | None |
| id | \`str \\ | None\` | None |
| classes | \`str \\ | None\` | None |
| tooltip | \`RenderableType \\ | None\` | None |

## **7\. Data Display & Selection Widgets (Conditional Inclusion)**

While the primary focus is on widgets that directly collect user input, some widgets primarily designed for data display can play a role in information collection through selection. The DataTable widget is a case in point. It is engineered for displaying tabular data efficiently.4 Direct user editing of individual cells, akin to an input field, is not its main design paradigm; programmatic updates are the standard way to modify its content.26 However, DataTable supports row or cell selection, and these selection events can be harnessed in a form context. For instance, a user might select a row from a DataTable (e.g., choosing a customer record), and the data from that selected row could then be used to populate other fields in a form or serve as the "value" for that part of the form. This makes DataTable relevant for information collection in an indirect, selection-driven manner.

### **7.1. DataTable Widget**

The DataTable widget is a powerful component for displaying data in a scrollable, sortable, and stylable table format.4 Each cell can contain Rich renderables, allowing for complex styling and content.

Key Attributes for Data Interaction/Selection:  
For using DataTable as a selection tool in forms, the following attributes are pertinent 26:

* cursor\_type (str): Determines what is selectable or navigable within the table. Options include "cell", "row", "column", or "none". For form selection, "row" or "cell" are typically most useful. Defaults to "cell".  
* cursor\_coordinate (Coordinate): A reactive attribute representing the current (row, column) position of the cursor.  
* show\_cursor (bool): Controls the visibility of the cursor within the table. Defaults to True.  
* Other attributes like fixed\_rows, fixed\_columns, and zebra\_stripes control the table's appearance and readability but are less directly involved in the selection mechanism itself.

Key Events/Messages for Selection:  
The DataTable emits several messages when different parts of the table are selected, which are key for using it as an input mechanism in forms 26:

* DataTable.CellSelected: Posted when a cell is selected (e.g., by clicking or pressing Enter when cursor\_type="cell"). The message includes coordinate and value of the selected cell.  
* DataTable.RowSelected: Posted when a row is selected (when cursor\_type="row"). The message includes the row\_key and information about the cursor\_row. This is often the most useful event for forms where an entire record is being chosen.  
* DataTable.ColumnSelected: Posted when a column is selected (when cursor\_type="column"). Includes column\_key. These events provide the necessary information (like a row key or cell value) that can then be used by the application to fetch the relevant data for the form.

Styling:  
DataTable offers various styling options, including zebra\_stripes for alternating row colors, fixed\_rows and fixed\_columns for sticky headers/columns, cell\_padding for readability, and individual styling of cells using Rich renderables.  
Use Cases in Forms (Indirect Collection):  
While not for direct cell-by-cell data entry by the user within the table itself as a primary form input method, DataTable can be very effective for:

* Displaying a list of existing records (e.g., customers, products, orders).  
* Allowing the user to select one record (row) from this table.  
* Using the data from the selected record to populate other fields in the current form or as the primary "value" collected by this part of the form (e.g., selecting a product ID to add to an order).

**Table: DataTable \- Key Selection Attributes & Events**

| Attribute/Event | Type | Description & Form Relevance for Selection |
| :---- | :---- | :---- |
| cursor\_type | str | "cell", "row", "column", "none". Determines what is selectable. "row" is often key for forms. |
| cursor\_coordinate | Coordinate | Current (row, column) of the cursor. |
| show\_cursor | bool | Visibility of the cursor. |
| DataTable.CellSelected | Event | Posted when a cell is selected. Provides value of the cell. |
| DataTable.RowSelected | Event | Posted when a row is selected. Provides row\_key. Crucial for selecting a record. |
| DataTable.ColumnSelected | Event | Posted when a column is selected. Provides column\_key. |

## **8\. Common Attributes, Styling Principles, and Validation**

Across the diverse range of Textual widgets available for information collection, several attributes, styling principles, and validation approaches are common or share underlying philosophies. Understanding these commonalities can simplify the development of the Formulator app by allowing for consistent handling of these aspects in its YAML schema.

### **8.1. Common Reactive Attributes**

Many Textual widgets, especially those used in forms, share a set of common reactive attributes that control their identification, styling, and basic behavior:

* name (str | None): An optional string used to name the widget. This can be particularly useful in form handling logic for identifying which widget's data is being processed or for mapping form fields to data models.5  
* id (str | None): An optional string that assigns a unique ID to the widget within the Document Object Model (DOM). This ID is primarily used for targeting the widget with Textual CSS rules or for querying it programmatically from the application code.5  
* classes (str | None): An optional string containing one or more space-separated CSS class names. These classes can be used to apply shared styles to multiple widgets or to group widgets for styling purposes.5  
* disabled (bool): A boolean attribute that, when True, makes the widget non-interactive. A disabled widget typically changes its appearance to indicate its state and does not respond to user input. This is a standard feature across almost all input and selection widgets.5  
* tooltip (RenderableType | None): An optional Rich renderable (e.g., a string or Text object) that provides help text displayed when the mouse cursor hovers over the widget.5  
* compact (bool): This attribute has been systematically added to a wide range of input and selection widgets, including Button, Input, Checkbox, RadioButton, RadioSet, OptionList, TextArea, Select, and SelectionList.7 When set to True, it typically renders the widget without borders and with reduced padding, resulting in a more condensed appearance. This is a conscious design decision by Textualize to offer a consistent way to achieve a minimalist aesthetic, simplifying the creation of denser UIs or forms where default borders might be visually overwhelming. Its boolean nature makes it easy to toggle this style. The Formulator app should consistently expose the compact attribute for all widgets that support it, providing users with a straightforward way to control this aspect of styling via YAML.

### **8.2. General Styling with Textual CSS**

Textual employs a CSS-like system for styling widgets, allowing for a high degree of customization over their appearance and layout.3 Styles can be defined in separate .tcss files or inline. Key aspects include:

* **Selectors:** Widgets can be targeted for styling using their type (e.g., Input), id (e.g., \#my-input), or classes (e.g., .form-field).  
* **Properties:** Many standard CSS properties are supported, such as border, padding, margin, width, height, background, color, text-align, display, layout, and dock.3  
* **Component Classes:** Many widgets define specific "component classes" (e.g., input--cursor, switch--slider) that allow for fine-grained styling of internal parts of the widget. These are crucial for detailed visual customization.  
* **Pseudo-classes:** Textual supports pseudo-classes like :hover, :focus, :disabled, and the validation-related \-valid and \-invalid classes, enabling dynamic styling based on widget state.

### **8.3. Validation Mechanisms**

Data validation is critical for ensuring the integrity of information collected through forms. Textual provides robust built-in validation capabilities, particularly for text-based inputs, while selection widgets often rely more on application-level logic post-selection.

* **Input and MaskedInput:**  
  * The Input widget offers comprehensive validation through its validators attribute (for custom rules), validate\_on (to control timing), valid\_empty (for optional fields), and the type attribute (for basic type checking like "integer" or "number").5  
  * The MaskedInput widget provides implicit validation through its template string, which enforces a specific structure on the input.9 It can also use the inherited validators for additional checks.  
* **Selection Widgets (Checkbox, Select, RadioSet, etc.):**  
  * For these widgets, the "input" is inherently constrained by the predefined set of options. Validation, therefore, often shifts from checking the format of free-form text to ensuring that a selection has been made (if the field is mandatory) or that the chosen value conforms to broader business rules.  
  * This distinction influences where validation logic is best placed. While Input and MaskedInput handle much of it internally, for selection widgets, the application often performs validation after a Changed or Selected event is received.  
* **Visual Feedback:** Textual automatically applies \-valid and \-invalid CSS classes to Input and MaskedInput widgets based on their validation status, allowing for immediate visual feedback (e.g., green or red borders). This is a key aspect of user-friendly form design.

The Formulator app's YAML schema could allow direct specification of validators for Input and MaskedInput. For selection widgets, it might focus on a "required" flag or similar simple constraints, with more complex validation logic being handled by the application code that consumes the form data, reacting to the change events from these widgets.

## **9\. Conclusion and Recommendations for Formulator App**

Textual provides a rich and continually evolving suite of widgets that are well-suited for collecting information in Terminal User Interfaces. From basic text entry and binary toggles to complex hierarchical selections and structured input masks, the library offers developers a powerful toolkit for building interactive and user-friendly forms. The Formulator app, by accurately and comprehensively mapping these features to its YAML interface, can significantly empower developers to build sophisticated terminal applications with greater ease and efficiency.

### **Summary of Key Information-Collecting Widgets**

* **Core Text Input:** Input (single-line text), TextArea (multi-line text), MaskedInput (structured/formatted text).  
* **Binary & Single Choice:** Checkbox (boolean), RadioSet (with RadioButtons for single selection from a group), Switch (on/off toggle), Select (dropdown single selection), OptionList (visible list single selection).  
* **Multiple Choice:** SelectionList (multiple selections from a visible list).  
* **Hierarchical/File Selection:** DirectoryTree (file/directory paths), Tree (custom hierarchical data).  
* **Form Actions:** Button (submitting forms, triggering actions).  
* **Data Display for Selection:** DataTable (selecting a row/cell from tabular data to inform other inputs).

### **Recommendations for Formulator YAML Schema**

To effectively leverage Textual's capabilities, the Formulator app's YAML schema should consider the following:

* **Widget Type Mapping:**  
  * Establish a clear and intuitive mapping from YAML keys (e.g., type: text\_input or type: dropdown\_select) to specific Textual widget classes (e.g., textual.widgets.Input, textual.widgets.Select).  
* **Attribute Exposure:**  
  * Prioritize exposing the key attributes identified in this report for each widget. This includes fundamental attributes like value (or its equivalent for data retrieval, e.g., pressed\_index for RadioSet, selected for SelectionList), placeholder, options (for selection widgets), label, variant (for Button), disabled, and compact.  
  * For Input and MaskedInput, ensure full support for validators, validate\_on, valid\_empty, type, restrict, and template (for MaskedInput).  
* **Event Handling:**  
  * Consider how Formulator will allow users to define actions or handlers for key events. This is crucial for dynamic forms. Options might include:  
    * Specifying application-defined callback function names to be invoked.  
    * A simplified action system within YAML that maps to common Textual actions or messages.  
  * Key events to consider are Input.Submitted, Button.Pressed, Select.Changed, Checkbox.Changed, RadioSet.Changed, Switch.Changed, SelectionList.SelectedChanged, Tree.NodeSelected, and DirectoryTree.FileSelected/DirectorySelected.  
* **Styling Abstractions:**  
  * Allow direct passthrough of id and classes attributes in YAML for users who want to apply custom Textual CSS.  
  * Universally expose the compact boolean attribute for all widgets that support it, providing a simple toggle for a common style.  
  * Optionally, offer higher-level styling abstractions in YAML (e.g., border\_style: heavy, text\_color: red) that map to common Textual CSS patterns or component class styling, simplifying common styling tasks for users less familiar with TCSS.  
* **Validation:**  
  * Provide clear mechanisms in YAML to define validators (perhaps as strings representing known validator types or references to custom validator functions) for Input and MaskedInput.  
  * Include a simple "required" flag for all input/selection fields that, when true, would trigger basic validation (e.g., ensuring an Input is not empty or a Select has a choice made).

### **Leveraging Textual's Strengths**

The Formulator app should encourage its users to leverage Textual's inherent strengths:

* Utilize semantic variants ("primary", "success", "warning", "error") for Button widgets to provide clear visual cues about button actions.  
* Promote the use of MaskedInput for fields requiring specific data formats, improving data quality at the source.  
* Highlight the utility of the compact style for creating modern, dense form layouts where appropriate.  
* Emphasize the power of Textual CSS for achieving highly customized form appearances.

By providing a well-structured and comprehensive YAML interface to these Textual widgets and their features, the Formulator app can significantly reduce the boilerplate code required for building forms in Textual, allowing developers to focus more on application logic and less on UI minutiae.

### **Table: Summary Comparison of Information Collection Widgets**

| Widget | Primary Use Case | Key Data Attribute(s) | Multi-Select Capable | Typical "Value" Collected |
| :---- | :---- | :---- | :---- | :---- |
| Input | Single-line text entry | value (str) | No | String |
| TextArea | Multi-line text entry | text (str) | No | String |
| MaskedInput | Structured single-line text entry | value (str) | No | Formatted String |
| Checkbox | Binary choice (on/off) | value (bool) | Yes (if used individually) | Boolean |
| RadioSet | Single choice from a group | pressed\_index (int), pressed\_button (RadioButton) | No | Index or value of selected RadioButton |
| Switch | Binary toggle (on/off) | value (bool) | No | Boolean |
| Select | Single choice from dropdown list | value (Any) | No | Value associated with selected option |
| OptionList | Single choice from visible list | OptionList.OptionSelected event (provides option/index) | No | Value/ID of selected option |
| SelectionList | Multiple choices from visible list | selected (list\[Any\]) | Yes | List of values of selected options |
| DirectoryTree | File or directory path selection | FileSelected/DirectorySelected event (provides path) | No | Path object |
| Tree | Single choice from hierarchical data | NodeSelected event (provides node with data) | No | Data/ID associated with selected node |
| Button | Triggering form actions | N/A (action, not data collection) | N/A | N/A (triggers event) |
| DataTable | Selecting a row/cell from tabular data | RowSelected/CellSelected event (provides key/value) | No (for a single event) | Key/data of selected row/cell |

#### **Works cited**

1. Textual, accessed May 26, 2025, [https://textual.textualize.io/](https://textual.textualize.io/)  
2. textual-inputs \- PyPI, accessed May 26, 2025, [https://pypi.org/project/textual-inputs/](https://pypi.org/project/textual-inputs/)  
3. Python Textual: Build Beautiful UIs in the Terminal, accessed May 26, 2025, [https://realpython.com/python-textual/](https://realpython.com/python-textual/)  
4. Widgets \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widget\_gallery/](https://textual.textualize.io/widget_gallery/)  
5. Input \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/input/](https://textual.textualize.io/widgets/input/)  
6. textual/CHANGELOG.md at main · Textualize/textual · GitHub, accessed May 26, 2025, [https://github.com/Textualize/textual/blob/main/CHANGELOG.md](https://github.com/Textualize/textual/blob/main/CHANGELOG.md)  
7. Releases · Textualize/textual \- GitHub, accessed May 26, 2025, [https://github.com/Textualize/textual/releases](https://github.com/Textualize/textual/releases)  
8. TextArea \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/text\_area/](https://textual.textualize.io/widgets/text_area/)  
9. MaskedInput \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/masked\_input/](https://textual.textualize.io/widgets/masked_input/)  
10. Checkbox \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/checkbox/](https://textual.textualize.io/widgets/checkbox/)  
11. RadioButton \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/radiobutton/](https://textual.textualize.io/widgets/radiobutton/)  
12. RadioSet \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/radioset/](https://textual.textualize.io/widgets/radioset/)  
13. Select \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/select/](https://textual.textualize.io/widgets/select/)  
14. OptionList \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/option\_list/](https://textual.textualize.io/widgets/option_list/)  
15. SelectionList \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/selection\_list/](https://textual.textualize.io/widgets/selection_list/)  
16. Android.Widget \- ToggleButton Class \- Learn Microsoft, accessed May 26, 2025, [https://learn.microsoft.com/en-us/dotnet/api/android.widget.togglebutton?view=net-android-35.0](https://learn.microsoft.com/en-us/dotnet/api/android.widget.togglebutton?view=net-android-35.0)  
17. Toggle button \- Intelligence Community Design System, accessed May 26, 2025, [https://design.sis.gov.uk/components/toggle-button/](https://design.sis.gov.uk/components/toggle-button/)  
18. ToggleButton (On/Off) Tutorial With Example In Android, accessed May 26, 2025, [https://abhiandroid.com/ui/togglebutton](https://abhiandroid.com/ui/togglebutton)  
19. Switch \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/switch/](https://textual.textualize.io/widgets/switch/)  
20. Widgets \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/](https://textual.textualize.io/widgets/)  
21. ListItem \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/list\_item/](https://textual.textualize.io/widgets/list_item/)  
22. ListView \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/list\_view/](https://textual.textualize.io/widgets/list_view/)  
23. DirectoryTree \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/directory\_tree/](https://textual.textualize.io/widgets/directory_tree/)  
24. Tree \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/tree/](https://textual.textualize.io/widgets/tree/)  
25. Button \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/button/](https://textual.textualize.io/widgets/button/)  
26. DataTable \- Textual, accessed May 26, 2025, [https://textual.textualize.io/widgets/data\_table/](https://textual.textualize.io/widgets/data_table/)  
27. Crash Course On Using Textual \- Fedora Magazine, accessed May 26, 2025, [https://fedoramagazine.org/crash-course-on-using-textual/](https://fedoramagazine.org/crash-course-on-using-textual/)
