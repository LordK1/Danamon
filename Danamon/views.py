from django.shortcuts import render

__author__ = 'k1'


def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, "about.html", context)
