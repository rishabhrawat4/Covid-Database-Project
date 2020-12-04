from django.urls import path
from . import views

urlpatterns = [
    path('', views.databasePage, name='databasePage')
]