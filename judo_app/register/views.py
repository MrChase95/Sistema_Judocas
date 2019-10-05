from rest_framework import generics, serializers
from .serializers import (StudentSerializer, UserSerializer,
                            TeacherSerializer, UserProfileSerializer,
                            ClassSerializer)

# Create your views here.


class StudentAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = StudentSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)


class TeacherAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = TeacherSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)


class UserProfileAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)


class ClassAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassSerializer
    queryset = ClassSerializer.Meta.model.objects.all()

    def perform_destroy(self, instance):
        print(instance.__dict__)

    def perform_update(self, serializer):
        print(serializer.validated_data)


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
