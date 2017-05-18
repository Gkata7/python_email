from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^email$', views.email),
    url(r'^results$', views.results),
    url(r'^email(?P<id>\d+)/delete$', views.delete)
]
