from django.shortcuts import render
from django.views.generic import TemplateView, ListView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'posts/index.html'
