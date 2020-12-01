from django.urls import path

from .views import mainpage, chosen_category, product_page


urlpatterns = [
    path('', mainpage, name='home'),
    path('catalog/<str:category>/', chosen_category, name='chosen_category'),
    path('catalog/<str:category>/<int:product_id>/', product_page, name='product_page')
]
