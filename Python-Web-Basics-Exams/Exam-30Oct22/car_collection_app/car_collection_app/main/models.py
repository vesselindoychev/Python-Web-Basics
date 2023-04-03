from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection_app.main.custom_validators import UsernameMinLengthValidator, CarCreationMaxYearValidator, \
    CarCreationMinYearValidator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 10
    USERNAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 18

    PASSWORD_MAX_LENGTH = 30

    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MAX_LENGTH = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            UsernameMinLengthValidator(USERNAME_MIN_LENGTH),
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    TYPE_MAX_LENGTH = 10

    MODEL_MAX_LENGTH = 20
    MODEL_MIN_LENGTH = 2

    CAR_CREATION_MAX_YEAR = 2049
    CAR_CREATION_MIN_YEAR = 1980

    PRICE_MIN_VALUE = 1

    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CAR_TYPES = (
        SPORTS_CAR,
        PICKUP,
        CROSSOVER,
        MINIBUS,
        OTHER
    )

    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=((car_type, car_type) for car_type in CAR_TYPES),
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=(
            MinLengthValidator(MODEL_MIN_LENGTH),
        ),
    )

    year = models.IntegerField(
        validators=(
            CarCreationMaxYearValidator(CAR_CREATION_MAX_YEAR),
            CarCreationMinYearValidator(CAR_CREATION_MIN_YEAR),
        ),
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )
