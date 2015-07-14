from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.FirstMessageView.as_view(), name='first'),
    url(r'^known/$', views.KnownUserView.as_view(), name='known'),
]