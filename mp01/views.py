from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.views import generic

#--- TemplateView
class HomeView(TemplateView):

    template_name = 'index.html'

def country(request, pk):
    return render(request, 'country.html', {'pk':pk})
