from django.urls import path
from photos.views import *

urlpatterns = [
    path('', gallery, name = 'gallery'),
    path('photo/<str:pk>/', viewPhoto, name = 'photo'),
    path('add/', addPhoto, name = 'add'),

]