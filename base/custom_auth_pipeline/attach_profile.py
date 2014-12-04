from base.models import Profile

def attach_profile(backend, user, response, *args, **kwargs):
    if user is not None and Profile.objects.filter(pk=user.id).count() == 0:
        profile = Profile()
        profile.user = user
        profile.save()