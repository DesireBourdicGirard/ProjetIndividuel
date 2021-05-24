from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('communautes/', views.communautes, name='toutes_communautes'),
    path('communautes/<int:communaute_id>', views.communaute, name='une_communaute'),
    path('communautes/<int:communaute_id>/<int:action>', views.communautes, name='toutes_communautes_modifs'),

]