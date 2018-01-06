from django import forms
from django.forms import fields
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserInfo
import re

class SignUpForm(forms.Form):
    password = fields.CharField(max_length=128, label='password', widget=forms.PasswordInput)
    re_password = fields.CharField(max_length=128, label='re_password', widget=forms.PasswordInput)
    email = fields.EmailField()
    username = fields.CharField()

    def clean_username(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError('password', forms.ValidationError(_("не менее 6 символов %s" % password), code="Invalid"))
        return password
    def clean(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        if password != re_password:
            self.add_error('re_password', forms.ValidationError(_("пароли не совпадают"), code="Invalid"))

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) <= 150 and len(username) >= 3:
            try:
                User.objects.get(username=username)
                raise forms.ValidationError(_('такой пользователь уже есть'))
            except ObjectDoesNotExist:
                return username
        else:
            raise forms.ValidationError(_('длина от 3 до 150 символов'))

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise forms.ValidationError(_('пользователь с таким email-ом уже существует'))
        except ObjectDoesNotExist:
            return email

    class Meta:
        model = UserInfo
        fields = ['password', 'email', 'username', 're_password']

class LogInForm(forms.Form):
    password = fields.CharField(max_length=128, label='password', widget=forms.PasswordInput)
    username = fields.CharField()
    error_message = _('неправильный логин или пароль')

    def confirm_login_allowed(self, user):
        pass
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            if re.search(r'@', username):
                return User.objects.get(email=username).username
        except ObjectDoesNotExist:
            raise forms.ValidationError(self.error_message)
        return username

    def clean_password(self):
        return self.cleaned_data['password']


    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            User.objects.get(username=username)
        except:
            raise forms.ValidationError(self.error_message)

    class Meta:
        models = User
        fields = ['password', 'username']