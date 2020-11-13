from django.shortcuts import render


def render_mainpage(request):
    return render(request, 'base.html')