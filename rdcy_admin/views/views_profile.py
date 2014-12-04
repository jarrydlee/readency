from django.views.generic import ListView
from base.models import Profile


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profile_list'
    template_name = 'rdcy_admin/profile_list.html'

   