from django.shortcuts import render
from . models import Home


def home(request):
    home = Home.objects.all()

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)

def _base(request):
    home = Home.objects.all()

    context = {
        'home': home,
    }

    return render(request, '_base.html', context)