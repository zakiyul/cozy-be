from django.urls import path
from . import views

urlpatterns = [
    path('recommended-spaces/', views.space_recomendation),
    path('recommended-spaces/<int:id>', views.detail_space_recomendation)
]