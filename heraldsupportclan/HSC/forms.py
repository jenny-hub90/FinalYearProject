from dataclasses import field
from django import forms
from .models import Question, Respose

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'autofocus': True,
                'placeholder':'How to create a Q&A webiste with Django?'
                
            })
        }

class NewResoponseForm(forms.ModelForm):
    class Meta:
        model = Respose
        fields = ['body']

 