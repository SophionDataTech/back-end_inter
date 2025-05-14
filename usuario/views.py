# usuarios/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer

class CadastroUsuario(APIView):
    def post(self, requisicao):
        try:
            serializer = UsuarioSerializer(data=requisicao.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'mensagem': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as erro:
            return Response("FALHA: {}".format(erro), 400)
