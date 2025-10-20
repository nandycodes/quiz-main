from django.urls import path
from . import views

urlpatterns = [
    path('perguntas/<str:nivel>/', views.listar_perguntas),  # Ex: /api/perguntas/facil/
    path('resultado/', views.salvar_resultado),               # Ex: /api/resultado/
]
