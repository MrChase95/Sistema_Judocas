from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r"^student/(?P<pk>[0-9])/$", views.StudentAPI.as_view(), name='student_api'),
    re_path(r"^user/(?P<pk>[0-9])/$", views.UserAPI.as_view(), name='user_api'),
    re_path(r"^userprofile/(?P<pk>[0-9])/$", views.UserProfileAPI.as_view(), name='userprofile_api'),
    re_path(r"^teacher/(?P<pk>[0-9])/$", views.UserAPI.as_view(), name='teacher_api'),
    re_path(r"^class/(?P<pk>[0-9])/$", views.ClassAPI.as_view(), name='class_api'),
    re_path("user_list/", views.UserListAPI.as_view(), name='user_list_api'),
    re_path("student_list/", views.StudentListAPI.as_view(), name='student_list_api'),
    re_path("userprofile_list/", views.UserProfileListAPI.as_view(), name='userprofile_list_api'),
    re_path("teacher_list/", views.TeacherListAPI.as_view(), name='teacher_list_api'),
    re_path("class_list/", views.ClassListAPI.as_view(), name='class_list_api'),
]