from django.shortcuts import render
from rest_framework import generics, renderers
# Create your views here.


class HomeView():
    template_name = 'home.html'


def HomeView_basic(request, *args, **kwargs):
    return render(request, "home.html", {})
