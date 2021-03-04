from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snacks

# Create your views here.
class SnacksListView(ListView):
    template_name = 'snacks.html'
    model = Snacks

class SnacksDetailView(DetailView):
    template_name = 'snack_details.html'
    model = Snacks
