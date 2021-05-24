from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

"""Local imports"""
from.models import Communaute, Post


@login_required
def communautes(request, communaute_id=0, action=0):
    """On sélectionne ici l'ensemble des communautés"""
    communautes = Communaute.objects.all()

    """Le marqueur d'action est par défaut à 0, lorsque l'utilisateur n'a rien cliqué sur aucun bouton d'abonnement"""
    if action == 1:
        """L'action 1 correspond à une requête d'abonnement de la part de l'utilisateur"""
        action_com = Communaute.objects.get(id=communaute_id)
        action_com.abonnes.add(request.user)
    elif action == 2:
        """L'action 2 correspond à une requête de désabonnement"""
        action_com = Communaute.objects.get(id=communaute_id)
        action_com.abonnes.remove(request.user)

    for communaute in communautes:
        abonnement = 0
        if request.user in communaute.abonnes.all():
            abonnement = 1
        communaute.user_abonne = abonnement

    return render(request, 'communities.html', locals())

@login_required
def communaute(request, communaute_id):
    posts = Post.objects.filter(id=communaute_id)
    communaute_choisie = Communaute.objects.get(id=communaute_id)

    return render(request, 'community.html', locals())
