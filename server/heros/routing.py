from django.urls import path
from django.conf.urls import include, url
from .consumers import WShero

ws_urlpatterns =[
    path('ws/', WShero),
]