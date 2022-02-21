from dataclasses import field
from tkinter import Widget
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


class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Respose
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'What are your thoughts?'
            })
        }

 