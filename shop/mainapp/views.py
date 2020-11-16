from django.shortcuts import render

from .models import Clothes


CATEGORY_TITLES = {'animals': 'Животные',
                   'games': 'Игры',
                   'russia': 'Россия'}

def render_mainpage(request):
    context = {
        'clothes': list(Clothes.objects.using('animals').all()) + \
                   list(Clothes.objects.using('games').all()) + \
                   list(Clothes.objects.using('russia').all()),
        'categories': CATEGORY_TITLES
    }
    return render(request, 'mainapp/show_clothes.html', context)

def render_chosen_category(request, **kwargs):
    return render(request, 'mainapp/show_clothes.html',
                  context={'chosen_category': CATEGORY_TITLES[kwargs['name']],
                           'clothes': Clothes.objects.using(kwargs['name']).all(),
                           'categories': CATEGORY_TITLES})
