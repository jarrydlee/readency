from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class AjaxRequiredMixin(object):
    # TODO
    def dispatch(self, request, *args, **kwargs):
        return super(AjaxRequiredMixin, self).dispatch(request, *args, **kwargs)