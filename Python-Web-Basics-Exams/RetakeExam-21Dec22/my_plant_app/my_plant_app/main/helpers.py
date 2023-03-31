from my_plant_app.main.models import Profile, Plant


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None
