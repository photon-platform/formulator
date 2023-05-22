class Validator:
    """
    Validator is a class containing static methods for validating form inputs.

    Each method in Validator takes the following parameters:
    - field_label: The label of the field being validated. Used in error messages.
    - value: The value of the field being validated.
    - validation_errors: A list to which any validation error messages should be appended.
    - rule_value: The value of the validation rule (e.g., minimum length, maximum length, etc.).

    The following validation rules are currently implemented:
    - required: Checks that the field is not empty or only whitespace.
    - min_length: Checks that the field's value is at least a certain number of characters long.
    - max_length: Checks that the field's value is not longer than a certain number of characters.
    - min_value: Checks that the field's value (cast to a float) is not less than a certain number.
    - max_value: Checks that the field's value (cast to a float) is not more than a certain number.
    - email: Checks that the field's value is a valid email address (contains an '@' and a '.').
    - numeric: Checks that the field's value is numeric (contains only digits).
    - alphabetic: Checks that the field's value is alphabetic (contains only letters).
    """
    @staticmethod
    def required(field_label, value, validation_errors, required):
        if required and not value.strip():
            validation_errors.append(f"{field_label} is required.")
    
    @staticmethod
    def min_length(field_label, value, validation_errors, min_length):
        if len(value) < min_length:
            validation_errors.append(
                f"{field_label} must be at least {min_length} characters long."
            )

    @staticmethod
    def max_length(field_label, value, validation_errors, max_length):
        if len(value) > max_length:
            validation_errors.append(
                f"{field_label} must be no more than {max_length} characters long."
            )

    @staticmethod
    def min_value(field_label, value, validation_errors, min_value):
        if value and float(value) < float(min_value):
            validation_errors.append(
                f"{field_label} must be at least {min_value}."
            )

    @staticmethod
    def max_value(field_label, value, validation_errors, max_value):
        if value and float(value) > float(max_value):
            validation_errors.append(
                f"{field_label} must be no more than {max_value}."
            )

    @staticmethod
    def email(field_label, value, validation_errors, is_email):
        if is_email:
            if "@" not in value or "." not in value:
                validation_errors.append(
                    f"{field_label} must be a valid email address."
                )

    @staticmethod
    def numeric(field_label, value, validation_errors, is_numeric):
        if is_numeric and not value.isnumeric():
            validation_errors.append(f"{field_label} must be a numeric value.")

    @staticmethod
    def alphabetic(field_label, value, validation_errors, is_alphabetic):
        if is_alphabetic and not value.isalpha():
            validation_errors.append(f"{field_label} must be an alphabetic value.")

