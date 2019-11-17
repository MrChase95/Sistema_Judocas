from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^student/$", views.StudentListAPI.as_view(), name='student_list_api'),
    re_path(r"^student/(?P<pk>[0-9])/$", views.StudentAPI.as_view(), name='student_api'),
    re_path(r"^user/$", views.UserListAPI.as_view(), name='user_list_api'),
    re_path(r"^user/(?P<pk>[0-9])/$", views.UserAPI.as_view(), name='user_api'),
    re_path(r"^userprofile/$", views.UserProfileListAPI.as_view(), name='userprofile_list_api'),
    re_path(r"^userprofile/(?P<pk>[0-9])/$", views.UserProfileAPI.as_view(), name='userprofile_api'),
    re_path(r"^teacher/$", views.TeacherListAPI.as_view(), name='teacher_list_api'),
    re_path(r"^teacher/(?P<pk>[0-9])/$", views.UserAPI.as_view(), name='teacher_api'),
    re_path(r"^tournament/$", views.TournamentListAPI.as_view(), name='tournament_list_api'),
    re_path(r"^tournament/(?P<pk>[0-9])/$", views.TournamentAPI.as_view(), name='tournament_api'),
    re_path(r"^participants/$", views.ParticipantsListAPI.as_view(), name='participants_list_api'),
    re_path(r"^participants/(?P<pk>[0-9])/$", views.ParticipantsAPI.as_view(), name='participants_api'),
    re_path(r"^competitor/$", views.CompetitorListAPI.as_view(), name='competitor_list_api'),
    re_path(r"^competitor/(?P<pk>[0-9])/$", views.CompetitorAPI.as_view(), name='competitor_api'),
    re_path(r"^referee/$", views.RefereeListAPI.as_view(), name='referee_list_api'),
    re_path(r"^referee/(?P<pk>[0-9])/$", views.RefereeAPI.as_view(), name='referee_api'),
    re_path(r"^knockout/$", views.KnockoutListAPI.as_view(), name='knockout_list_api'),
    re_path(r"^knockout/(?P<pk>[0-9])/$", views.KnockoutAPI.as_view(), name='knockout_api'),
    re_path(r"^token/$", views.get_csrf_token, name='csrf_token'),
]