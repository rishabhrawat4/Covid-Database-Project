from django.urls import path
from . import views

urlpatterns = [
    path('searchdatabase', views.databasePage, name='databasePage'),
    path('', views.homepage, name='homepage'),
    path('contact-us', views.contactUs, name='contactUs'),

]