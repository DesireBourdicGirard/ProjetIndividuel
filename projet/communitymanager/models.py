from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Communaute(models.Model):
    nom = models.CharField(max_length=150)
    abonnes = models.ManyToManyField(User)

    class Meta:
        verbose_name = "communaute"
        ordering = ['nom']

    def __str__(self):
        return self.nom

class Priorite(models.Model):
    nom = models.CharField(max_length=25)

    class Meta:
        verbose_name = "priorite"
        ordering = ['nom']

    def __str__(self):
        return self.nom

class Post(models.Model):
    titre = models.CharField(max_length=150)
    description = models.CharField(max_length=1500, blank=True, null=True)
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date de création")
    communaute = models.ForeignKey('Communaute', on_delete=models.CASCADE)
    priorite = models.ForeignKey('Priorite', on_delete=models.CASCADE)
    evenementiel = models.BooleanField()
    date_evenement = models.DateField(null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "post"
        ordering = ['titre']

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    texte = models.CharField(max_length=500)
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "commentaire"
        ordering = ['auteur']

    def __str__(self):
        return self.texte