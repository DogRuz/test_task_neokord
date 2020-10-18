from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='new_number'),
    url(r'^post-form/?$', views.post_form, name='post_form'),
]
