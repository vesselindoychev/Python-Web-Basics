from django.contrib import admin

from petstagram.main.models import Pet, PetPhoto


@admin.register(Pet)
class Pet(admin.ModelAdmin):
    pass


@admin.register(PetPhoto)
class PetPhoto(admin.ModelAdmin):
    pass
