from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^your-name/$', views.get_name, name='name'),
]