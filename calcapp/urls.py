from django.conf.urls import patterns, url
from calcapp import views


urlpatterns = patterns('',
    url(r'^$', views.querySave, name='querySave'),
    )