from django.views.generic import View
from django.views.generic.base import ContextMixin
from django.shortcuts import render

from rdcy_mixins.login_required_mixin import LoginRequiredMixin
from base.models import Profile

class ProfileView(LoginRequiredMixin, ContextMixin, View):
    template = 'rdcy_platform/home.html'
    profile = None

    def get(self, request):
        self.profile = request.user.profile

        context = self.get_context_data()
        return render(request, self.template, context)


