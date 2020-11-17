from django.shortcuts import render

from .models import Clothes
from .services.utils import get_page_obj_for_page_number


CATEGORY_TITLES = {'animals': 'Животные',
                   'games': 'Игры',
                   'russia': 'Россия'}

ITEMS_PER_PAGE = 9

def mainpage(request):
    items = list(Clothes.objects.using('animals').all()) + \
            list(Clothes.objects.using('games').all()) + \
            list(Clothes.objects.using('russia').all())
    page_obj = get_page_obj_for_page_number(request.GET.get('page', 1),
                                            ITEMS_PER_PAGE,
                                            items)
    return render(request, 'mainapp/show_clothes.html',
                  {'page_obj': page_obj,
                   'categories': CATEGORY_TITLES})

def chosen_category(request, **kwargs):
    page_obj = get_page_obj_for_page_number(request.GET.get('page', 1),
                                            ITEMS_PER_PAGE,
                                            Clothes.objects.using(kwargs['category']).all())
    return render(request, 'mainapp/show_clothes.html',
                  context={'chosen_category': CATEGORY_TITLES[kwargs['category']],
                           'category':kwargs['category'],
                           'page_obj': page_obj,
                           'categories': CATEGORY_TITLES})

def clothes_page(request, **kwargs):
    print(kwargs['category'], kwargs['clothes_id'])
    clothes_data = Clothes.objects.using(kwargs['category']).get(id=kwargs['clothes_id'])
    return render(request, 'mainapp/clothes_page.html',
                  context={'clothes_data':clothes_data})
