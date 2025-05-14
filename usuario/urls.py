# usuarios/urls.py
from django.urls import path
from .views import CadastroUsuario

urlpatterns = [
    path('cadastrar/', CadastroUsuario.as_view(), name='cadastrar_usuario'),
]
