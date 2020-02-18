from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
    return render(request, 'portfolio/index.html', {})

def about(request):
    return render(request, "portfolio/about.html", {})

def experience(request):
    return render(request, "portfolio/experience.html", {})


def education(request):
    return render(request, "portfolio/education.html", {})


def skills(request):
    return render(request, "portfolio/skills.html", {})


def languages(request):
    return render(request, "portfolio/languages.html", {})


def certification(request):
    return render(request, "portfolio/certification.html", {})