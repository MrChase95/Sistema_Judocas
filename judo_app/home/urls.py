from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r"^$", views.HomeView.as_view(), name='home'),

]