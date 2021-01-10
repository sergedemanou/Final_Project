from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('newthread/', views.newthread, name='newthread'),
    path('newcomment/<int:id>', views.newcomment, name='newcomment'),
]