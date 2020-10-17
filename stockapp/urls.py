from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='trader-home-page'),
    path('calc', views.calc, name='calc-page'),
    path('thing', views.thing, name='thing-page'),
    path('things', views.things, name='things-page'),
]