from django.urls import path

from . import views

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('rooms/', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
]