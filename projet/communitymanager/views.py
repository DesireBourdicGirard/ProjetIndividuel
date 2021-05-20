from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

"""Local imports"""
from.models import Communaute, Post


# Create your views here.
@login_required
def communautes(request):
    """On sélectionne ici l'ensemble des communautés"""
    communautes = Communaute.objects.all()


    for communaute in communautes:
        abonnement = 0
        if request.user in communaute.abonnes.all():
            abonnement = 1
        communaute.user_abonne = abonnement

    return render(request, 'registration/communities.html', locals())

@login_required
def communaute(request, communaute_id):

    posts = get_object_or_404(Post, id=communaute_id)
    communaute_choisie = Communaute.objects.get(id=communaute_id)

    return render(request, 'registration/community.html', locals())
