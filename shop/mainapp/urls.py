from django.urls import path

from .views import mainpage, chosen_category, clothes_page


urlpatterns = [
    path('', mainpage, name='home'),
    path('catalog/<str:category>/', chosen_category, name='chosen_category'),
    path('catalog/<str:category>/<int:clothes_id>/', clothes_page, name='clothes_page')
]
