from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone


#Local imports
from .models import Communaute, Post, Commentaire
from .forms import FormComment, FormEcrirePost


@login_required
def communautes(request, communaute_id=0, action=0):
    """Cette vue affiche l'ensemble des communautés et permet à l'utilisateur de s'abonner et de se désabonner"""
    #On sélectionne ici l'ensemble des communautés"""
    communautes = Communaute.objects.all()

    #Le marqueur d'action est par défaut à 0, lorsque l'utilisateur n'a rien cliqué sur aucun bouton d'abonnement
    if action == 1:
        #L'action 1 correspond à une requête d'abonnement de la part de l'utilisateur
        action_com = Communaute.objects.get(id=communaute_id)
        action_com.abonnes.add(request.user)
    elif action == 2:
        #L'action 2 correspond à une requête de désabonnement
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
    """Cette vue affiche l'ensemble des posts d'une communauté, et leurs principales caractéristiques"""
    posts = Post.objects.filter(communaute_id=communaute_id)
    communaute_affichee = Communaute.objects.get(id=communaute_id)

    return render(request, 'community.html', locals())

@login_required
def post(request, post_id):
    """On affiche ici le contenu du post et les commentaires associés"""
    post = get_object_or_404(Post, id=post_id)

    # On affiche ici le commentaire associé au post
    commentaires = Commentaire.objects.filter(post__id=post_id)

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

    return render(request, 'post.html', locals())


@login_required
def ecrire_post(request):
    """Ecrire un nouveau post grâce au formulaire de post"""
    print("in view")
    sauvegarde = False
    if request.method == "POST":
        post_form = FormEcrirePost(request.POST or None)
        print("in post")
        if post_form.is_valid():
            post_ecrit = post_form.save(commit=False)
            post_ecrit.auteur = request.user
            post_ecrit.save()
            sauvegarde = True
            print("valid")
            post_id = post_ecrit.id
            return redirect('un_post', post_id)
    else:
        post_form = FormEcrirePost()
        print("in else")
    return render(request, 'ecrire_post.html', locals())


@login_required
def post_edit(request, post_id):
    """Modification d'un post"""

    form = FormEcrirePost(request.POST or None)
    if form.is_valid():
        post_a_modifier = get_object_or_404(Post, post__id=post_id)
        post_a_modifier = form.save()
        post_a_modifier.save()

    return render(request, 'post.html', post_a_modifier)

def posts(request):
    posts = Post.objects.all()

    return render(request, 'posts.html', locals())