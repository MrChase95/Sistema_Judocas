from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r"^$", views.StudentAPI.as_view(), name='student_api'),

]