from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from rest_framework import generics, serializers

from .serializers import (StudentSerializer, UserSerializer,
                          TeacherSerializer, UserProfileSerializer,
                          ClassSerializer, TournamentSerializer, ParticipantsSerializer,
                          KnockoutSerializer, CompetitorSerializer, RefereeSerializer,
                          )


# Create your views here.

def get_csrf_token(request):
    return HttpResponse(get_token(request))


class StudentAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = StudentSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class TeacherAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = TeacherSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class UserProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class ClassAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassSerializer
    queryset = ClassSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class TournamentAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TournamentSerializer
    queryset = TournamentSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class ParticipantsAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParticipantsSerializer
    queryset = ParticipantsSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class CompetitorAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompetitorSerializer
    queryset = CompetitorSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class RefereeAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RefereeSerializer
    queryset = RefereeSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class KnockoutAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KnockoutSerializer
    queryset = KnockoutSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)
        serializer.save()


class UserListAPI(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.run_validation(serializer.validated_data)
        if serializer.is_valid():
            serializer.save()


class ClassListAPI(generics.ListCreateAPIView):
    serializer_class = ClassSerializer
    queryset = ClassSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()


class StudentListAPI(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = StudentSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()


class TeacherListAPI(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = TeacherSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()


class UserProfileListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()


class TournamentListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = TournamentSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()


class ParticipantsListAPI(generics.ListCreateAPIView):
    serializer_class = ParticipantsSerializer
    queryset = ParticipantsSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()


class KnockoutListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = KnockoutSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()


class CompetitorListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = CompetitorSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()


class RefereeListAPI(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = RefereeSerializer.Meta.model.objects.all()

    def perform_create(self, serializer: serializers.BaseSerializer):
        print(serializer.validated_data)
        serializer.save()
