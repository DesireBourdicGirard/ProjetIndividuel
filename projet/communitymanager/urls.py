from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('communautes/', views.communautes, name='toutes_communautes'),
    path('communautes/<int:communaute_id>', views.communaute, name='une_communaute'),
    path('communautes/<int:communaute_id>/<int:action>', views.communautes, name='toutes_communautes_modifs'),
    path('post/<int:post_id>', views.post, name='un_post'),
    path('post/ecrire_post', views.ecrire_post, name='ecrire_post'),
    path('posts/', views.posts, name='tous_posts'),
]