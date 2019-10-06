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

        first_part: str = cpf_to_str[:9]
        first_digit: str = cpf_to_str[9:10]
        second_digit: str = cpf_to_str[10:11]
        if int(first_digit) != (sum(int(digit) * weight
                                   for digit, weight in zip(first_part,
                                                            digits_weight[0])) * 10) % 11:
            raise serializers.ValidationError('CPF not Valid')
        if int(second_digit) != (sum(int(digit) * weight
                                   for digit, weight in zip(first_part + first_digit,
                                                            digits_weight[1])) * 10) % 11:
            raise serializers.ValidationError('CPF not Valid')
        return value


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
