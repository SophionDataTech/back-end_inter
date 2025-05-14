# backend/permissions.py
from rest_framework.permissions import BasePermission
from django.conf import settings

class TokenGlobalValido(BasePermission):
    def has_permission(self, request, view):
        token_recebido = request.headers.get('Authorization')
        token_esperado = f'Token {settings.TOKEN_API}'
        return token_recebido == token_esperado
