from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from .models import UserInfo
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
import re

from .forms import SignUpForm, LogInForm

class Index(generic.View):
    template_name = 'app/index.html'
    def get(self, request):
        if request.user.is_authenticated:
            username = request.user.get_username()
            return render(request, self.template_name, {'is_auth': 'true', 'username': username})
        return render(request, self.template_name, {'is_auth': ''})

def logout_user(request):
    if User.is_authenticated:
        logout(request)
    return redirect('/')

class FormAuth:
    c = {}
    template_name = ''
    form_class = None

    def get_form(self, request, errors=None):
        self.c.update(csrf(request))
        form = self.form_class(None)
        context = {'form': form, 'c': self.c}

        if errors == None:
            return render(request, self.template_name, context)

        return render(request, self.template_name, context, context.update({'errors': errors}))

class SignUp(generic.View, FormAuth):
    form_class = SignUpForm
    template_name = 'app/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return self.get_form(request)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            User.objects.create_user(email=email, password=password, username=username)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        e = form.errors
        return self.get_form(request, e)

class LogIn(generic.View, FormAuth):
    template_name ='app/login.html'
    form_class= LogInForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/signup')

        return self.get_form(request)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = self.form_class(request.POST)

        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']

            auth = authenticate(request, username=username, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('/')
            else:
                return self.get_form(request, form.error_message)
        err = form.errors.get('__all__')
        return self.get_form(request, err)
