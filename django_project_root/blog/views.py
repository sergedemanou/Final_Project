from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import *


def home(request):
    
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def designer(request):
    utilisateur = request.user
    #profil_utilisateur = Profile.objects.get(id=utilisateur.id)
    profil_utilisateurs = Profile.objects.filter(role="designer")
    print(profil_utilisateurs.all())

    context={'utilisateurs':profil_utilisateurs}
    return render(request, 'blog/designer.html', context)

def dev_mobile(request):
    utilisateur = request.user
    #profil_utilisateur = Profile.objects.get(id=utilisateur.id)
    profil_utilisateurs = Profile.objects.filter(role="developpeur")
    print(profil_utilisateurs.all())

    context={'utilisateurs':profil_utilisateurs}
    return render(request, 'blog/dev_mobile.html', context)

def dev_web(request):
    utilisateur = request.user
    #profil_utilisateur = Profile.objects.get(id=utilisateur.id)
    profil_utilisateurs = Profile.objects.filter(role="developpeur")
    print(profil_utilisateurs.all())

    context={'utilisateurs':profil_utilisateurs}

    return render(request, 'blog/dev_web.html', context)





def voir_profil_dev(request, id):
    profil = Profile.objects.get(id=id)
    user = profil.user
    

    return render(request, 'blog/voir_profil_dev.html', {'user':user})

def voir_profil_des(request, id):
    profil = Profile.objects.get(id=id)
    user = profil.user
    

    return render(request, 'blog/voir_profil_des.html', {'user':user})


def policy(request):
    return render(request, 'blog/policy.html')

