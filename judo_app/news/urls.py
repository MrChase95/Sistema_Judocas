from django.urls import path
from . import views

urlpatterns = [
    path("", views.NewsView, name="news-list"),
    path("noticias/<int:pk>/", views.News_DetailView, name="news-detail"),
    path("noticias/<int:pk>/edit/", views.News_Edit, name="news-edit"),
    path("noticias/nova/", views.News_NewView, name="news-new")
]
