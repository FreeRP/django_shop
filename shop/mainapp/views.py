from django.shortcuts import render

from .models import Clothes, Category
from .services.utils import get_page_obj_for_page_number


CATEGORY_TITLES = {'animals': 'Животные',
                   'games': 'Игры',
                   'russia': 'Россия'}
ITEMS_PER_PAGE = 9

def mainpage(request):
    category_objects = [Category(slug=slug, name=name,
                                 image_name=Clothes.objects.using(slug).get(id=1).img_name)
                        for slug, name in CATEGORY_TITLES.items()]
    return render(request, 'mainapp/main.html',
                  {'categories': category_objects})

def chosen_category(request, **kwargs):
    page_obj = get_page_obj_for_page_number(request.GET.get('page', 1),
                                            ITEMS_PER_PAGE,
                                            Clothes.objects.using(kwargs['category']).all())
    return render(request, 'mainapp/chosen_category.html',
                  context={'chosen_category': CATEGORY_TITLES[kwargs['category']],
                           'category':kwargs['category'],
                           'page_obj': page_obj,
                           'categories': CATEGORY_TITLES})

def product_page(request, **kwargs):
    product_data = Clothes.objects.using(kwargs['category']).get(id=kwargs['product_id'])
    return render(request, 'mainapp/product.html',
                  context={'product_data': product_data,
                           'categories': CATEGORY_TITLES})
