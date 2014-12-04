from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from base.models import Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'api_endpoint', 'is_active']
    template_name = 'rdcy_admin/service_create_form.html'

    def form_invalid(self, form):
        response = super(ServiceCreateView, self).form_invalid(form)
        return response

    def form_valid(self, form):
        return super(ServiceCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('service_create')

