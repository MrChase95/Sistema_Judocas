from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from rest_framework import generics, views
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import Response

from .serializers import (StudentSerializer, UserSerializer,
                          TeacherSerializer, UserProfileSerializer,
                          ClassSerializer, TournamentSerializer, ParticipantsSerializer,
                          KnockoutSerializer, CompetitorSerializer, RefereeSerializer,
                          ProfileSerializer, CategorySerializer, DojoSerializer, TournamentProfileSerializer)


# Create your views here.

def get_csrf_token(request):
    return HttpResponse(get_token(request))


class StudentAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = StudentSerializer.Meta.model.objects.all()


class TeacherAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = TeacherSerializer.Meta.model.objects.all()


class UserProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileSerializer.Meta.model.objects.all()


class TournamentProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TournamentProfileSerializer
    queryset = TournamentProfileSerializer.Meta.model.objects.all()


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()


class ClassAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassSerializer
    queryset = ClassSerializer.Meta.model.objects.all()


class TournamentAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TournamentSerializer
    queryset = TournamentSerializer.Meta.model.objects.all()


class ParticipantsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParticipantsSerializer
    queryset = ParticipantsSerializer.Meta.model.objects.all()


class CompetitorAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompetitorSerializer
    queryset = CompetitorSerializer.Meta.model.objects.all()


class RefereeAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RefereeSerializer
    queryset = RefereeSerializer.Meta.model.objects.all()


class KnockoutAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KnockoutSerializer
    queryset = KnockoutSerializer.Meta.model.objects.all()


class UserListAPI(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()


class ProfileListAPI(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()


class ProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = ProfileSerializer.Meta.model.objects.all()


class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = CategorySerializer.Meta.model.objects.all()


class CategoryAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = CategorySerializer.Meta.model.objects.all()


class ClassListAPI(generics.ListCreateAPIView):
    serializer_class = ClassSerializer
    queryset = ClassSerializer.Meta.model.objects.all()


class StudentListAPI(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = StudentSerializer.Meta.model.objects.all()


class TeacherListAPI(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = TeacherSerializer.Meta.model.objects.all()


class UserProfileListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileSerializer.Meta.model.objects.all()


class TournamentProfileListAPI(generics.ListCreateAPIView):
    serializer_class = TournamentProfileSerializer
    queryset = TournamentProfileSerializer.Meta.model.objects.all()


class TournamentListAPI(generics.ListCreateAPIView):
    serializer_class = TournamentSerializer
    queryset = TournamentSerializer.Meta.model.objects.all()


class ParticipantsListAPI(generics.ListCreateAPIView):
    serializer_class = ParticipantsSerializer
    queryset = ParticipantsSerializer.Meta.model.objects.all()


class KnockoutListAPI(generics.ListCreateAPIView):
    serializer_class = KnockoutSerializer
    queryset = KnockoutSerializer.Meta.model.objects.all()


class CompetitorListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = CompetitorSerializer.Meta.model.objects.all()


class RefereeListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = RefereeSerializer.Meta.model.objects.all()


class DojoAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DojoSerializer
    queryset = DojoSerializer.Meta.model.objects.all()


class DojoListAPI(generics.ListCreateAPIView):
    serializer_class = DojoSerializer
    queryset = DojoSerializer.Meta.model.objects.all()


class UserTemplateView(views.APIView):
    template_name = 'user_control.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, pk):
        return Response()


class UserProfileTemplateView(views.APIView):
    template_name = 'user_profile_control.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, pk):
        return Response()


class ClassTemplateView(views.APIView):
    template_name = 'class_control.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, pk):
        return Response()


class DojoTemplateView(views.APIView):
    template_name = 'dojo_control.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, pk):
        return Response()


class TournamentTemplateView(views.APIView):
    template_name = 'tournament_control.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, pk):
        return Response()


class ParticipantsTemplateView(views.APIView):
    template_name = 'participants_control.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, pk):
        return Response()


class KnockoutTemplateView(views.APIView):
    template_name = 'knockout_control.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, pk):
        return Response()
