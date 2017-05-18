from django.conf.urls import url
from consumer import views

urlpatterns = [
    url(r'^$', views.MessageView.as_view(), name='index'),
]
