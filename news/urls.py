from django.urls import path
from . import views

urlpatterns = [
    path("", views.NewsView, name="news-list"),
    path("noticia/<int:pk>/", views.News_DetailView, name="news-detail"),
    path("noticia/<int:pk>/edit/", views.News_Edit, name="news-edit"),
    path("noticia/nova/", views.News_NewView, name="news-new")
]
