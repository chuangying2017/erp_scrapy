from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('get_fiction/', views.fiction_class, name='fiction_class'),
    path('post_fiction_create/', views.fiction, name='fiction_create'),
    path('post_fiction_chapter/', views.fiction_chapter, name='fiction_chapter'),
]
