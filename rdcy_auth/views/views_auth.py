from django.views.generic import View
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pocket import Pocket
from rdcy_auth.forms import LoginForm
from urllib.parse import quote_plus
from base.models import Profile


class PocketAuthenticationView(View):
    redirect_uri = quote_plus('http://127.0.0.1:8000/oauth/pocket/')

    def get(self, request):
        if request.session.get('request_token'):
            request_token = request.session.get('request_token')
            del request.session['request_token']

            user_credentials = Pocket.get_credentials(consumer_key=settings.POCKET_CONSUMER_KEY, code=request_token)
            access_token = user_credentials['access_token']
            email = user_credentials['username']

            try:
                user = User.objects.get(username=access_token)
            except User.DoesNotExist:
                # If doesn't exist create new user
                user = User.objects.create_user(
                    username=access_token,
                    email=email,
                    password=access_token
                    )

                # Save our permanent code for later.
                profile = Profile()
                profile.user = user
                profile.access_token = access_token
                profile.save()

            user = authenticate(
                username=access_token,
                password=access_token
                )
            login(request, user)

        return redirect('/')

    def post(self, request):

        request_token = Pocket.get_request_token(consumer_key=settings.POCKET_CONSUMER_KEY, redirect_uri=self.redirect_uri)
        request.session['request_token'] = request_token

        # URL to redirect user to, to authorize your app
        auth_url = Pocket.get_auth_url(code=request_token, redirect_uri=self.redirect_uri)
        
        return redirect(auth_url)

class LoginView(View):
    template_name = 'rdcy_auth/login.html'

    def get(self, request):
        return render(request, self.template_name)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


