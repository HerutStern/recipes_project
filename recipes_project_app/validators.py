from rest_framework.exceptions import ValidationError


def validator_level(value):
    levels = ['easy', 'medium', 'hard']
    if value not in levels:
        raise ValidationError(f'{value} id not a valid level')