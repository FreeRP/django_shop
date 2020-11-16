from django.urls import path

from .views import render_mainpage, render_chosen_category


urlpatterns = [
    path('', render_mainpage, name='home'),
    path('catalog/<str:category>/', render_chosen_category, name='chosen_category')
]
