from django import forms
from base.models import Service, ServiceConnection

class ServiceConnectionUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceConnectionCreateForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.all()
        self.fields['service'].label_from_instance = lambda obj: obj.name

    class Meta():
        model = ServiceConnection
        fields = ['service', 'num_articles']
        exclude = ('profile',)

