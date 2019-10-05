from django.shortcuts import render
from rest_framework import generics
# Create your views here.

class HomeView(generics.ListAPIView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, args)