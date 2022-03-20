from django import forms
from .models import Author, ForumPost
# from django import form


class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")

        # widgets = {
        #     'title': forms.TextInput(attrs={'class:': 'form-control'}),
        #     'bio': forms.Textarea(attrs={'class:': 'form-control'}),
        #     'profile_pic': forms.URLInput(attrs={'class:': 'form-control'}),
            
        #  }


class ForumPostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = ["title", "content", "categories", "tags" ]

        # widget = {
        #     'title': forms.TextInput(attrs={'class:': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class:': 'form-control'}),
        #     'categories': forms.Select(attrs={'class:': 'form-control'}),
        #     'tags': forms.TextInput(attrs={'class:': 'form-control'}),
        # }