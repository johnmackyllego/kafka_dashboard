from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from consumer import views

urlpatterns = [
    url(r'^$', views.MessageView.as_view(), name='home'),
    url(r'^aa/', include('consumer.urls', namespace = 'consumer')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]
