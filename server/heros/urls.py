from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import AllHeros, Hero

urlpatterns = [
    url(r'^all-heros$', AllHeros.as_view()),
    url(r'^hero/(?P<hero_id>[0-9]+)', Hero.as_view()),
]