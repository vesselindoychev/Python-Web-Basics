from django.contrib import admin

from petstagram.main.models import Profile, Pet, PetPhoto


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class Pet(admin.ModelAdmin):
    pass


@admin.register(PetPhoto)
class PetPhoto(admin.ModelAdmin):
    pass
