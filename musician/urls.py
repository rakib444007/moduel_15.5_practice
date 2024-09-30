from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('musician/',views.musician, name='musician'),
    path('musician_delete/<int:id>',views.musician_delete, name='musician_delete'),
    path('musician_edit/<int:id>',views.musician_edit, name='musician_edit'),
]
