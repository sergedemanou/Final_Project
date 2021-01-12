from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('newthread/', views.newthread, name='newthread'),
    path('newcomment/<int:id>', views.newcomment, name='newcomment'),
    path('searchbar/', views.searchbar, name='searchbar'),
    # path('delete_post/<int:id>', views.delete_post, name='delete_post'),
]