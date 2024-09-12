
from . views import hello_word
from django.urls import path

urlpatterns = [
    path('', hello_word, name='hello_world'),
]