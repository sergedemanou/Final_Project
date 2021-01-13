from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.viewlogin, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete_f/', views.delete_f, name='delete_f'),
    path('delete_p/', views.delete_p, name='delete_p'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)