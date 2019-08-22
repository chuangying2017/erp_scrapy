from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('get_fiction/', views.fiction_class, name='fiction_class')
]
