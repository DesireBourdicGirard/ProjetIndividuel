from django import forms
from .models import Commentaire, Post

class FormComment(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('texte',)

class FormEcrirePost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('auteur',)

