from django.shortcuts import render
from rest_framework import renderers
from django.views.generic import TemplateView
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


class AdminView(TemplateView):
    template_name = 'admin_page.html'
    renderer_classes = [renderers.TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


def HomeView_basic(request, *args, **kwargs):
    return render(request, "home.html", {})
