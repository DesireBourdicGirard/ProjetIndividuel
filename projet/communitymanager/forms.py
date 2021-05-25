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

    def clean(self):
        """
        Validates a new album only if it's not a duplicate
        """
        cleaned_data = super(FormEcrirePost, self).clean()
        evenementiel = cleaned_data['evenementiel']
        date_evenementiel = cleaned_data['date_evenementiel']

        if evenementiel and not date_evenementiel:
            raise forms.ValidationError('Un évenement doit avoir une date spécifiée')
        return cleaned_data