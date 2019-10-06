"""judo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('register/', include('register.urls')),
    re_path('home/', include('home.urls')),
    re_path('', include('home.urls')),
    re_path(r'^docs/', include_docs_urls(title='My API title', public=False)),
    path('openapi/', get_schema_view(
        title="Sistema Judocas",
        description="Pagina de Testes das APIs",
        version="1.0.0"
    ), name='openapi-schema'),
]
