from django.shortcuts import render

__author__ = 'k1'


def about(request):
    return render(request, "about.html", {})
