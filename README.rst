Formulator: Dynamic Form Builder
================================

Formulator is a Python-based terminal form application built using the Textual
library and YAML. It allows you to quickly define and generate terminal-based
forms using a simple YAML blueprint. Formulator also provides basic input
validation features that can be customized as needed.


Installation
------------
To install Formulator, clone this repository and install the required Python packages:

.. code-block:: bash

    git clone https://github.com/yourusername/formulator.git
    cd formulator
    pip install -r requirements.txt


Usage
-----
To use Formulator, first create a YAML blueprint for your form. This blueprint
defines the fields, buttons, and validation rules for your form. An example
blueprint is included in the repository.

To run the form application with your blueprint, use the following command:

.. code-block:: bash

    python formulator.py --blueprint blueprint.yaml

Customization
=============
To customize Formulator, you can define your own validation rules in the
blueprint. Each validation rule corresponds to a method in the Formulator class
that is called when the form is submitted. The method name must follow the
format 'validate_{rule}', where {rule} is the name of the validation rule in
the blueprint.

For example, if you want to add a validation rule that checks if a field's
value is a valid URL, you can add the rule 'url: true' to the field's
'validate' section in the blueprint:

.. code-block:: yaml

    fields:
      website:
        label: Website
        placeholder: Enter your website URL
        type: Input
        validate:
          url: true

Then, in the Formulator class, define a method 'validate_url' that performs the
desired validation check:

.. code-block:: python

    def validate_url(self, field_label, value, validation_errors, is_url):
        if is_url:
            # Check if the value is a valid URL.
            # Add an error message to validation_errors if the check fails.
            pass

With this setup, Formulator will automatically call the 'validate_url' method
when the form is submitted and the 'website' field has a value.

Using Formulator as a Library
=============================

Formulator can also be imported and used in your Python scripts. This allows
you to dynamically generate forms and handle user input within your
application. Here is a basic usage example:

.. code-block:: python

    from formulator import Formulator
    import yaml

    # Load a form blueprint from a YAML file
    with open('blueprint.yaml', 'r') as file:
        blueprint = yaml.load(file, Loader=yaml.FullLoader)

    # Create and run the form
    form = Formulator(blueprint)
    return_values = form.run()

    # Use the returned values as needed
    print(return_values)

In this example, `run()` starts the form application and returns the user's
input when the form is submitted. The input is returned as a dictionary where
the keys are the field IDs and the values are the user's input.

If you want to define the blueprint in Python instead of a YAML file, you can
build it as a nested dictionary. Here is an example:

.. code-block:: python

    blueprint = {
        'form': {
            'title': 'Form Title',
            'fields': {
                'first-name': {
                    'label': 'First Name',
                    'placeholder': 'Enter your First Name',
                    'type': 'Input',
                    'validate': {
                        'required': True
                    }
                },
                'last-name': {
                    'label': 'Last Name',
                    'placeholder': 'Enter your Last Name',
                    'type': 'Input',
                    'validate': {
                        'required': True
                    }
                }
            },
            'buttons': {
                'save': {
                    'label': 'Save'
                },
                'quit': {
                    'label': 'Quit'
                }
            }
        }
    }

    # Create and run the form
    form = Formulator(blueprint)
    return_values = form.run()

    # Use the returned values as needed
    print(return_values)

This blueprint creates a form with two text fields ('First Name' and 'Last
Name') and two buttons ('Save' and 'Quit'). When the 'Save' button is clicked,
the form will validate the input (checking that both fields are filled in), and
then return the input.


Contact
=======
For questions, issues, or feature requests, please open an issue on the Formulator GitHub repository.

