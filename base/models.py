from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    access_token = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ServiceConnection(models.Model):
    profile = models.ForeignKey('Profile')
    service = models.ForeignKey('Service')
    num_articles = models.IntegerField(default=3)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.service.name)

class Service(models.Model):
    name = models.CharField(max_length=100)
    api_endpoint = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Article(models.Model):
    profile = models.ForeignKey('Profile')
    service = models.ForeignKey('Service')
    service_item_id = models.IntegerField()
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

