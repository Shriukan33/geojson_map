from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MainMapView(TemplateView):
    template_name = "carte/carte.html"
