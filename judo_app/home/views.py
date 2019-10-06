from django.shortcuts import render
from rest_framework import generics, renderers
# Create your views here.


class HomeView():
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, args)