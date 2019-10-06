from django.contrib import admin
from .models import User, UserProfile, Student, Teacher, Category, Profile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Category)
admin.site.register(Profile)
