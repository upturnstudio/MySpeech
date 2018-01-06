from django.conf.urls import url
from django.views.generic.edit import FormMixin
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^signup$', views.SignUp.as_view(),name='signup'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^login$', views.LogIn.as_view(), name='login')
]