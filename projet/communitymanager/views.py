from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone


"""Local imports"""
from .models import Communaute, Post, Commentaire
from .forms import FormComment, FormEcrirePost


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
    communaute_affichee = Communaute.objects.get(id=communaute_id)

    return render(request, 'community.html', locals())

@login_required
def post(request, post_id):
    """On affiche ici le contenu du post"""
    post = get_object_or_404(id=post_id)

    # On affiche ici le commentaire associé au post
    commentaires = Commentaire.objects.filter(id=post_id)

    # Gestion du formulaire d'ajout d'un nouveau commentaire
    sauvegarde = False
    form = FormComment(request.POST or None)

    # Prise en compte de la communaute
    communaute_id = post.communaute.id

    if form.is_valid():
        commentaire = form.save(commit=False)
        commentaire.auteur = request.user
        commentaire.post = post
        commentaire.save()
        sauvegarde = True

    return render(request, 'communitymanager/post.html', locals())


@login_required
def ecrire_post(request):
    """Ecrire un nouveau post grâce au formulaire de post"""

    sauvegarde = False

    if request.method == "POST":
        form = FormEcrirePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.save()
            sauvegarde = True
            post_id = post.id

            return redirect('post', post_id)

    else:
        form = FormEcrirePost()

    return render(request, 'communitymanager/ecrire_post.html', locals())

@login_required
def post_edit(request, post_id):
    """Modification d'un post"""

    form = FormEcrirePost(request.POST or None)
    if form.is_valid():
        post_a_modifier = get_object_or_404(Post, id=post_id)
        post_a_modifier = form.save()
        post_a_modifier.save()

    return render(request, 'communitymanager/post.html', post_a_modifier)

def posts(request):
    posts = Post.objects.all()

    return render(request, 'communitymanager/posts.html', posts)