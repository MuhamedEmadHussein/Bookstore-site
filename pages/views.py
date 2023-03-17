from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"