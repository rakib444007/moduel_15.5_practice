from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('album/',views.album, name='album'),
    path('album_edit/<int:id>',views.album_edit, name='album_edit'),
]
