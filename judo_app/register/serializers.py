from rest_framework import serializers
from .models import Student, User, Teacher, UserProfile, Class, Profile
from typing import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_cpf(self, value):
        digits_weight: List[List[int]] = [
            [10, 9, 8, 7, 6, 5, 4, 3, 2],
            [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        ]
        cpf_to_str: str = str(value)
        if len(cpf_to_str) < 11:
            raise serializers.ValidationError('CPF must contains 11 digits')

        return value


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
