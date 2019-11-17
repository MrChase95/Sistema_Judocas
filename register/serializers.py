from typing import *

from rest_framework import serializers

from .models import (Student, User, Teacher, UserProfile, Class,
                     Tournament, Participants, Competitor, Referee
, Knockout)


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

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

    def validate_cpf(self, value):
        digits_weight: List[List[int]] = [
            [10, 9, 8, 7, 6, 5, 4, 3, 2],
            [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        ]
        cpf_to_str: str = str(value)
        if len(cpf_to_str) < 11:
            raise serializers.ValidationError('CPF must contains 11 digits')

        if cpf_to_str in ("11111111111", "22222222222", "33333333333", "44444444444",
                          "55555555555", "66666666666", "77777777777", "88888888888", "99999999999", "00000000000"):
            raise serializers.ValidationError('CPF not Valid')

        first_part: str = cpf_to_str[:9]
        first_digit: str = cpf_to_str[9:10]
        second_digit: str = cpf_to_str[10:11]
        aux: int = 0
        for digit, weight in zip(first_part, digits_weight[0]):
            aux += int(digit) * weight
        aux = aux % 11
        if(aux < 2):
            aux = 0
        elif(aux >= 2):
            aux = 11 - aux

        if int(first_digit) != aux:
            raise serializers.ValidationError('CPF not Valid')

        aux = 0
        for digit, weight in zip(first_part+first_digit, digits_weight[1]):
            aux += int(digit) * weight
        aux = aux % 11

        if(aux < 2):
            aux = 0
        elif(aux >= 2):
            aux = 11 - aux

        if int(second_digit) != aux:
            raise serializers.ValidationError('CPF not Valid')

        return value


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'


class CompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitor
        fields = '__all__'


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'


class KnockoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knockout
        fields = '__all__'
