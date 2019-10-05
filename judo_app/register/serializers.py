from rest_framework import serializers
from .models import Student, User, Teacher, UserProfile, Class, Profile


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, attrs):
        """
        Validate data for students Model
        :param attrs: Data to be validate
        :return: data if no validation error is raised
        """
        if attrs['profile'] is None or 'profile' not in attrs:
            raise serializers.ValidationError('Profile is required')
        if attrs['user'] is None or 'user' not in attrs:
            raise serializers.ValidationError('User is required')
        if not User.objects.get(user__id__exact=attrs['user']).is_active:
            raise serializers.ValidationError('User is not active')
        if not Profile.objects.get(id__exact=attrs['profile']).is_active:
            raise serializers.ValidationError('Profile is not Available')



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


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
