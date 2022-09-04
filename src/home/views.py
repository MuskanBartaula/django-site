from django.shortcuts import render
import random


def home(request):
    context = {
        "title": "Random Generator",
        "value": random.randint(0,9)
    }
    return render(request, "index.html", context) 
