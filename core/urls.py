from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('leads/', views.lista_leads, name='lista_leads'),
    path('leads/nova/', views.criar_lead, name='criar_lead'),
]