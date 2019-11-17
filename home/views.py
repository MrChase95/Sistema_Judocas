from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import renderers


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class LoginView(TemplateView):
    template_name = 'registration/login.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, *args)


def HomeView_basic(request, *args, **kwargs):
    return render(request, "home.html", {})
