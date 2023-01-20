from django.urls import path
from . import views

urlpatterns = [
    path('recommended-spaces/', views.space_recomendation)  
]