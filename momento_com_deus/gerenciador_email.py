# utils/email_utils.py
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class UserManager:
    def __init__(self):
        pass

    def enviar_email_para_usuario(self, usuario, assunto, corpo):
        """Envia um email para um único usuário."""
        try:
            send_mail(
                assunto,
                corpo,
                settings.EMAIL_HOST_USER,
                [usuario.email],
                fail_silently=False,
            )
            print(f"Email enviado para {usuario.email}")
            return True
        except Exception as e:
            print(f"Erro ao enviar email para {usuario.email}: {e}")
            return False

    def processar_e_enviar_emails_usuarios(self):
        """Obtém usuários e envia o mesmo email para cada um."""
        usuarios = self.obter_emails_para_disparo()
        assunto = "Momento com Deus - " + datetime.today().strftime("%d/%m")
        corpo = "Por enquanto apenas um teste."
        for usuario in usuarios:
            self.enviar_email_para_usuario(usuario, assunto, corpo)

    def obter_emails_para_disparo(self):
        """Obtém uma lista de emails da base de dados."""
        # obter todos os emails de usuários ativos
        return User.objects.filter(is_active=True).values_list('email', flat=True)


# ====================================================================================

user_manager = UserManager()
user_manager.processar_e_enviar_emails_usuarios()