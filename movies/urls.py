from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('movies/', movies, name="movies"), 
    path('video/', video, name="video"),
]