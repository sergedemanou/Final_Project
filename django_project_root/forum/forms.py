from django.forms import ModelForm

from .models import *
from django import forms


class createThread(ModelForm):
    class Meta:
        model = Thread
        fields = "__all__"


class createComment(forms.Form):

    text = forms.CharField()

    """class Meta:
        model = Comment
        fields = ["text"]"""

# class Delete_post(request, pk):
#     template = 'forum/delete_post.html'
#     post = get_object_or_404()