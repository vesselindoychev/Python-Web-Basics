from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameMinLengthValidator:
    MIN_LENGTH_ERROR_MESSAGE = 'The username must be a minimum of 2 chars'

    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError(self.MIN_LENGTH_ERROR_MESSAGE)


@deconstructible
class CarCreationMaxYearValidator:
    CAR_CREATION_MIN_YEAR = 1980
    CAR_CREATION_MAX_YEAR = 2049
    CAR_CREATION_YEAR_ERROR_MESSAGE = f'Year must be between {CAR_CREATION_MIN_YEAR} and {CAR_CREATION_MAX_YEAR}'

    def __init__(self, car_creation_year):
        self.car_creation_year = car_creation_year

    def __call__(self, value):
        if value > self.car_creation_year:
            raise ValidationError(self.CAR_CREATION_YEAR_ERROR_MESSAGE)
        # if self.car_creation_year < value:
        #     raise ValidationError(self.CAR_CREATION_YEAR_ERROR_MESSAGE)


@deconstructible
class CarCreationMinYearValidator:
    CAR_CREATION_MIN_YEAR = 1980
    CAR_CREATION_MAX_YEAR = 2049
    CAR_CREATION_YEAR_ERROR_MESSAGE = f'Year must be between {CAR_CREATION_MIN_YEAR} and {CAR_CREATION_MAX_YEAR}'

    def __init__(self, car_creation_year):
        self.car_creation_year = car_creation_year

    def __call__(self, value):
        if value < self.car_creation_year:
            raise ValidationError(self.CAR_CREATION_YEAR_ERROR_MESSAGE)


@deconstructible
class DisabledFieldsFormMixin:
    disabled_fields = ()
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            field.widget.attrs['readonly'] = 'readonly'
