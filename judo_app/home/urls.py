from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # re_path(r"^$", views.HomeView.as_view(), name='home'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]