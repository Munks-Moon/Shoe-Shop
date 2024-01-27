from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact')
]