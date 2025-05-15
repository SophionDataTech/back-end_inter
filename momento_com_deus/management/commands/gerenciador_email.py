# utils/email_utils.py
import mailtrap as mt
import requests
import json
from django.core.management.base import BaseCommand
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    def __init__(self):
        pass

    def enviar_email_para_usuario(self, usuario, assunto, corpo):
        """Envia um email para um único usuário."""
        try:
            url = settings.EMAIL_URL

            payload = json.dumps({
                "from": {"email": settings.EMAIL_API, "name": "Intercessao Teste"},
                "to": [{"email": ""}],
                "subject": assunto,
                "text": corpo,
                "category": "Integration Test"
            })
            headers = {
            "Authorization": "Bearer " + settings.EMAIL_API_TOKEN,
            "Content-Type": "application/json"
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            
            print(f"Email enviado para {usuario}")
            return True
        except Exception as e:
            print(f"Erro ao enviar email para {usuario[0]}: {e}")
            return False

    def handle(self, *args, **options):
        """Obtém usuários e envia o mesmo email para cada um."""
        usuarios = self.obter_emails_para_disparo()
        assunto = "Momento com Deus - " + datetime.today().strftime("%d/%m")
        for usuario in usuarios:
            corpo = "Oi, {}! Tudo bem?\nPor enquanto apenas um teste :)".format(usuario[1])
            self.enviar_email_para_usuario(usuario, assunto, corpo)

    def obter_emails_para_disparo(self):
        """Obtém uma lista de emails da base de dados."""
        # obter todos os emails de usuários ativos
        return User.objects.filter(is_active=True).values_list('email', 'nome')

