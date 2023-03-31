from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.main.custom_validators import validate_first_letter_should_be_capital, validate_only_letters


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2

    FIRST_NAME_MAX_LENGTH = 20

    LAST_NAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
        )
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validate_first_letter_should_be_capital,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validate_first_letter_should_be_capital,
        )
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Plant(models.Model):
    TYPE_MAX_LENGTH = 14

    NAME_MAX_LENGTH = 20
    NAME_MIN_LENGTH = 2

    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    PLANTS_TYPES = (
        OUTDOOR_PLANTS,
        INDOOR_PLANTS,
    )

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=((t, t) for t in PLANTS_TYPES)
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    image = models.URLField()

    description = models.TextField()

    price = models.FloatField()
