import datetime

from django.contrib.auth import get_user_model
from django.db import models

from petstagram.accounts.models import PetstagramUser

UserModel = get_user_model()


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    ANIMAL_TYPES = (
        CAT,
        DOG,
        BUNNY,
        PARROT,
        FISH,
        OTHER,
    )

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(t) for t in ANIMAL_TYPES),
        choices=((t, t) for t in ANIMAL_TYPES),
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    def __str__(self):
        return f"{self.name} the {self.type}"

    class Meta:
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(

        ),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
