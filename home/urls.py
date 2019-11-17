from django.urls import re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # path("", views.HomeView_basic, name='home'),
    re_path(r"^$", views.HomeView.as_view(), name='home'),
    re_path(r"^login_screen/$", views.LoginView.as_view(), name='login_screen'),
    re_path(r'^swagger-ui/$', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
