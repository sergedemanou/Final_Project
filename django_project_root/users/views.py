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
        user_profile = Profile(user=utilisateur)
        user_profile.save()

        return redirect("login")
    return render(request, 'users/register.html')



def viewlogin(request):
    if request.method == "POST":
        username = request.POST.get("inputUsername")
        pwd = request.POST.get("inputPassword")
        utilisateurs = User.objects.filter(username=username, password=pwd)
        print(utilisateurs)
        print(username)
        print(pwd)
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
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

        f_form = FormationForm(request.POST)
        pr_form = ProjetsForm(request.POST)
        if f_form.is_valid() and pr_form.is_valid():
            f_form.save()
            pr_form.save()

    else:
        u_form = UserUpdateForm(instance=request.user) # cette ligne indique qu'on recupère l'user qui est cpnnecté et on met à jour son profil
        p_form = ProfileUpdateForm(instance=request.user.profile)
        f_form = FormationForm()
        pr_form = ProjetsForm()


    context = {
        'u_form': u_form,
        'p_form': p_form,
        'f_form': f_form,
        'pr_form': pr_form,
    }
    return render(request, 'users/profile.html', context)



def logout(request):
    auth.logout(request)
    return redirect('/')


# def formation(request):
#     context = {}
#     # creating a formset
#     FormationFormSet = formset_factory(FormationForm)
#     formset = FormationFormSet(request.POST or None)
#     # print formset data if it is valid
#     if formset.is_valid():
#         for form in formset:
#             save()
#     # Add the formset to context dictionary
#     context['formset'] = formset
#     return render(request, "users/profile.html", context)
#
# def projets(request):
#     context = {}
#     # creating a formset
#     ProjetsFormSet = formset_factory(ProjetsForm)
#     formset1 = ProjetsFormSet(request.POST or None)
#     # print formset data if it is valid
#     if formset1.is_valid():
#         for form in formset1:
#             print(form.cleaned_data)
#     # Add the formset to context dictionary
#     context['formset'] = formset1
#     return render(request, "users/profile.html", context)