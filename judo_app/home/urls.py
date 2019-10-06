from django.urls import re_path, path
from . import views


urlpatterns = [
    path("", views.HomeView, name='home'),
]
