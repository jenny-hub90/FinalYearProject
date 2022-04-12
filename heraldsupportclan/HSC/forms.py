from django import forms
from .models import Author, ForumPost
# from django import form


class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")

    


class ForumPostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = ["title", "content", "categories", "tags" ]

      