# usuarios/serializers.py
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'password', 'data_nascimento', 'sexo', 'cidade', 'uf']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, dados_validados):
        usuario = Usuario.objects.create_user(**dados_validados)
        return usuario
