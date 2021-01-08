from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FormationForm, ProjetsForm
from django.forms import formset_factory
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate



def register(request):
    if request.method == "POST":
        name = request.POST.get("inputLastName")
        firstname = request.POST.get("inputFirstName")
        username = request.POST.get("inputUsername")
        password = request.POST.get("inputPassword")
        email = request.POST.get("inputEmailAddress")
        cfpwd = request.POST.get("inputConfirmPassword")
        utilisateur = User.objects.create_user(last_name=name, first_name=firstname, username=username, password=password, email=email)
        utilisateur.save()
        user_profile = Profile(user=utilisateur, role=request.POST.get("exampleRadios"))
        print()
        user_profile.save()

        return redirect("login")
    return render(request, 'users/register.html')



def viewlogin(request):
    if request.method == "POST":
        username = request.POST.get("inputUsername")
        pwd = request.POST.get("inputPassword")
        utilisateurs = User.objects.filter(username=username, password=pwd)
        if len(utilisateurs) > 0:
            request.session['username'] = utilisateurs[0].username
            request.session['email'] = utilisateurs[0].email

        user = authenticate(request, username= username, password =pwd)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('blog-home')

        return redirect('login')
    return render(request, 'users/login.html')





@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)  # l'instance sert de modifier ou agir sur l'object fourni
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            print('validformation1')
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

        f_form = FormationForm(request.POST)
        pr_form = ProjetsForm(request.POST)
        if f_form.is_valid():
            print('validformation')
            f = Formation(intitulé = f_form.cleaned_data.get('intitulé'),# ici nous devons recupérer les champs un par un parce qu'on a fait un exclude de profile_id dans le formulaire de FormationForm
                          établissement = f_form.cleaned_data.get('établissement'),
                          description = f_form.cleaned_data.get('description'),
                          date_de_début = f_form.cleaned_data.get('date_de_début'),
                          date_de_fin = f_form.cleaned_data.get('date_de_fin'),
                          domaine = f_form.cleaned_data.get('domaine'),
                          diplômes_obtenus = f_form.cleaned_data.get('diplômes_obtenus'),
                          langages_de_programmation = f_form.cleaned_data.get('langages_de_programmation'),
                          profile_id = request.user.profile
                          )
            print("after object creation")
            f.save()
            return redirect('profile')

        if pr_form.is_valid():
            pr = Projets(intitulé=pr_form.cleaned_data.get('intitulé'),
                         période=pr_form.cleaned_data.get('période'),
                         lien=pr_form.cleaned_data.get('lien'),
                         profile_id=request.user.profile

            )
            pr.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user) # cette ligne indique qu'on recupère l'user qui est cpnnecté et on met à jour son profil
        p_form = ProfileUpdateForm(instance=request.user.profile)
        f_form = FormationForm()
        pr_form = ProjetsForm()

    formation_data = Formation.objects.all()
    projets_data = Projets.objects.all()
    print(formation_data)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'f_form': f_form,
        'pr_form': pr_form,
        'formation_data': formation_data,
        'projets_data': projets_data,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')


