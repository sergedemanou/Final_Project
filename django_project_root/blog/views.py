from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def designer(request):
    return render(request, 'blog/designer.html')

def dev_mobile(request):
    return render(request, 'blog/dev_mobile.html')

def dev_web(request):
    return render(request, 'blog/dev_web.html')

def programmeur(request):
    return render(request, 'blog/programmeur.html')

def policy(request):
    return render(request, 'blog/policy.html')

