from django.core.exceptions import ValidationError

FIRST_LETTER_MUST_BE_CAPITAL_ERROR_MESSAGE = 'Your name must start with a capital letter!'
ONLY_LETTERS_ERROR_MESSAGE = 'Plant name should contain only letters!'


def validate_first_letter_should_be_capital(value):
    if value[0].islower():
        raise ValidationError(FIRST_LETTER_MUST_BE_CAPITAL_ERROR_MESSAGE)


def validate_only_letters(value):
    if not all(ch.isalpha() for ch in value):
        raise ValidationError(ONLY_LETTERS_ERROR_MESSAGE)
