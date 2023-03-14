from django.http import HttpResponse
from django.template import loader
from calculator_app import calculator
from .forms import Energy
from django.shortcuts import render


def index(request):
    # template = loader.get_template()
    form_energy = Energy()
    # context = calculator([1518, 1071, 968], 0.95871974, "Industrial")

    return render(request, 'index.html', {'form': form_energy})
