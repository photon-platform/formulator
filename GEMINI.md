# Formulator

A library for dynamically generating terminal-based forms from YAML blueprints.

## Overview

The Formulator library interprets a YAML blueprint to generate an interactive Textual form. It handles input validation and error display, providing a simple way to collect structured user input in the terminal.

## Index

-   `formulator.py`: Core `Formulator` class that builds the form.
-   `composer.py`: The `Composer` class, responsible for widget layout.
-   `validator.py`: Handles data validation based on blueprint rules.
-   `formulator_modal.py`: A modal dialog implementation for forms.
-   `*.css`: Stylesheets for the form widgets.