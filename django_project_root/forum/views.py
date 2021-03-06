from django.shortcuts import render, redirect
from .models import *
from .forms import *
from blog.models import *
from users.models import *
from forum.models import *

# Create your views here.
#.discussion_set.all()

def index(request):
    threads = Thread.objects.all()
    count = threads.count()
    discussions = []
    for i in threads:
        discussions.append(i)

    context = {'forums': threads,
               'count': count,
               'discussions': discussions}
    return render(request, 'index.html', context)


def newthread(request):
    form = createThread()
    if request.method == 'POST':
        form = createThread(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newthread')
    context = {'form': form}
    return render(request, 'newthread.html', context)


def newcomment(request, id):
    form = createComment()
    comments = Comment.objects.filter(thread_id=id)
    user = request.user
    if request.method == 'POST':
        form = createComment(request.POST)
        if form.is_valid():
            thread = Thread.objects.get(id=id)
            coment = Comment(text=form.cleaned_data.get('text'), thread_id=thread, user_id=request.user )
            coment.save()
            return redirect('newcomment', id)
    context = {'form': form, 'comments': comments, 'user':user}
    return render(request, 'newcomment.html', context)

# def delete_post(request, id):

def searchbar(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        posts = Profile.objects.filter(role__contains=search)
        return render (request, 'searchbar.html', {'posts': posts})

    return render(request, 'searchbar.html', {'posts': None})

