from django.shortcuts import render
from rest_framework import generics
# Create your views here.


def HomeView(request, *args, **kwargs):
    return render(request, "home.html", {})
