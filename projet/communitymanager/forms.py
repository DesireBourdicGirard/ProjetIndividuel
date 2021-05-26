from django import forms
from .models import Commentaire, Post


class FormComment(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('texte',)


class FormEcrirePost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('auteur', 'date_creation',)

    def __init__(self, *args, **kwargs):
        super(FormEcrirePost, self).__init__(*args, **kwargs)
        self.fields['description'].queryset = self.instance.description
