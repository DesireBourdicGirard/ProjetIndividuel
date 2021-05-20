from datetime import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Communaute(models.Model):
    nom = models.CharField(max_length=200)
    abonnes = models.ManyToManyField(User)

    class Meta:
        verbose_name = "communaute"
        ordering = ['nom']

    def __str__(self):
        return self.nom

class Priorite(models.Model):
    nom = models.CharField(max_length=15)

    class Meta:
        verbose_name = "priorite"
        ordering = ['nom']

    def __str__(self):
        return self.nom

class Post(models.Model):
    label = models.CharField(max_length=200)
    contenu = models.CharField(max_length=2000, blank=True, null=True)
    date_creation = models.DateTimeField(default=timezone.utc)
    communaute = models.ForeignKey('Communaute', on_delete=models.CASCADE)
    priorite = models.ForeignKey('Priorite', on_delete=models.CASCADE)
    evenementiel = models.BooleanField()
    date_evenement = models.DateTimeField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "post"
        ordering = ['date_creation']

    def __str__(self):
        return self.label