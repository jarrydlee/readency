from django.views.generic import ListView
from django.shortcuts import render

from base.models import Service, ServiceConnection

from rdcy_mixins.login_required_mixin import LoginRequiredMixin

class ServiceConnectionView(LoginRequiredMixin, ListView):
    template_name = 'rdcy_platform/connections.html'
    queryset = Service.objects.filter(is_active=True).prefetch_related('serviceconnection_set')

    # This will have to change to either show fake serviceconnections 
    # left join service and connections

    def get(self, request):
        self.object_list = self.get_queryset().filter(serviceconnection__profile_id=request.user.id)

        context = self.get_context_data()
        return render(request, self.template_name, context)