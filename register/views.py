from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import (StudentSerializer, UserSerializer,
                          TeacherSerializer, UserProfileSerializer,
                          ClassSerializer, TournamentSerializer, ParticipantsSerializer,
                          KnockoutSerializer, CompetitorSerializer, RefereeSerializer,
                          ProfileSerializer, CategorySerializer, DojoSerializer,
                          TournamentProfileSerializer)


# Create your views here.

def get_csrf_token(request):
    return HttpResponse(get_token(request))


class StudentAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = StudentSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TeacherAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = TeacherSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class UserProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TournamentProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TournamentProfileSerializer
    queryset = TournamentProfileSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ClassAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassSerializer
    queryset = ClassSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TournamentAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TournamentSerializer
    queryset = TournamentSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ParticipantsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParticipantsSerializer
    queryset = ParticipantsSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class CompetitorAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompetitorSerializer
    queryset = CompetitorSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class RefereeAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RefereeSerializer
    queryset = RefereeSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class KnockoutAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KnockoutSerializer
    queryset = KnockoutSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class UserListAPI(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ProfileListAPI(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = CategorySerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class CategoryAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = CategorySerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ClassListAPI(generics.ListCreateAPIView):
    serializer_class = ClassSerializer
    queryset = ClassSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class StudentListAPI(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = StudentSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TeacherListAPI(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = TeacherSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class UserProfileListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TournamentProfileListAPI(generics.ListCreateAPIView):
    serializer_class = TournamentProfileSerializer
    queryset = TournamentProfileSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class TournamentListAPI(generics.ListCreateAPIView):
    serializer_class = TournamentSerializer
    queryset = TournamentSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ParticipantsListAPI(generics.ListCreateAPIView):
    serializer_class = ParticipantsSerializer
    queryset = ParticipantsSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class KnockoutListAPI(generics.ListCreateAPIView):
    serializer_class = KnockoutSerializer
    queryset = KnockoutSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class CompetitorListAPI(generics.ListCreateAPIView):
    serializer_class = CompetitorSerializer
    queryset = CompetitorSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class RefereeListAPI(generics.ListCreateAPIView):
    serializer_class = RefereeSerializer
    queryset = RefereeSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class DojoAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DojoSerializer
    queryset = DojoSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class DojoListAPI(generics.ListCreateAPIView):
    serializer_class = DojoSerializer
    queryset = DojoSerializer.Meta.model.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class UserTemplateView(generics.ListAPIView):
    template_name = 'user_control.html'
    renderer_classes = [TemplateHTMLRenderer]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # @login_required(login_url='/home/login/')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'user': request.user})


class UserProfileTemplateView(generics.ListAPIView):
    template_name = 'user_profile_control.html'
    renderer_classes = [TemplateHTMLRenderer]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # @login_required(login_url='/home/login/')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'user': request.user})


class ClassTemplateView(generics.ListAPIView):
    template_name = 'class_control.html'
    renderer_classes = [TemplateHTMLRenderer]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # @login_required(login_url='/home/login/')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'user': request.user})


class DojoTemplateView(generics.ListAPIView):
    template_name = 'dojo_control.html'
    renderer_classes = [TemplateHTMLRenderer]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # @login_required(login_url='/home/login/')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'user': request.user})


class TournamentTemplateView(generics.ListAPIView):
    template_name = 'tournament_control.html'
    renderer_classes = [TemplateHTMLRenderer]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # @login_required(login_url='/home/login/')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'user': request.user})


class ParticipantsTemplateView(generics.ListAPIView):
    template_name = 'participants_control.html'
    renderer_classes = [TemplateHTMLRenderer]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # @login_required(login_url='/home/login/')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'user': request.user})


class KnockoutTemplateView(generics.ListAPIView):
    template_name = 'knockout_control.html'
    renderer_classes = [TemplateHTMLRenderer]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # @login_required(login_url='/home/login/')
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'user': request.user})
