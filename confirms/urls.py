from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/notifications/$', views.sendTotification, name="Notification")
]

urlpatterns = format_suffix_patterns(urlpatterns)