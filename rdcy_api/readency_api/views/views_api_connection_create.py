from django.views.generic import View
from django.shortcuts import get_object_or_404

from rdcy_mixins import JSONResponseMixin
from base.models import Service, ServiceConnection


class ServiceConnectionCreateApi(JSONResponseMixin, View):

    def _update_or_create(self, request, service_id, is_active, num_articles):
        service = get_object_or_404(Service, pk=service_id)
        profile = request.user.profile

        return ServiceConnection.objects.update_or_create(
            service=service, 
            profile=profile,
            defaults={
                'is_active': is_active,
                'num_articles': num_articles
            })


    def post(self, request):
        context = {'status': 'ok'}

        if not request.is_ajax() and not request.POST:
            context.update({'status': 'failed'})
            return self.render_to_json_response(context, status_code=400)

        service_id = request.POST.get('service_id')
        is_active = request.POST.get('is_active') in ['true', '1']
        num_articles = request.POST.get('num_articles', 3)

        if service_id is not None and is_active is not None:
            service_connection, created = self._update_or_create(request, service_id, is_active, num_articles)

            context.update({
                'service_connection':service_connection.service.name
            })

        return self.render_to_json_response(context)