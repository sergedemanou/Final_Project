from django.urls import path
from  . import views

urlpatterns = [
    path('',views.home, name='blog-home'),
    path('about/',views.about, name='blog-about'),
    path('designer/',views.designer, name='designer'),
    path('dev_mobile/',views.dev_mobile, name='dev_mobile'),
    path('dev_web/',views.dev_web, name='dev_web'),
    path('voir_profil_dev/<int:id>',views.voir_profil_dev, name='voir_profil_dev'),
    path('voir_profil_des/<int:id>',views.voir_profil_des, name='voir_profil_des'),
    path('policy/',views.policy, name='policy'),

]
