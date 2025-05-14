from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class GerenciadorUsuario(BaseUserManager):
    """
    Classe para validar dados básicos e fazer o registro em BD.
    """
    def create_user(self, email, senha=None, **campos_extras):
        if not email:
            raise ValueError('O email é obrigatório')
        if not campos_extras.get('nome'):
            raise ValueError('O nome é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **campos_extras)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, senha=None, **campos_extras):
        campos_extras.setdefault('is_staff', True)
        campos_extras.setdefault('is_superuser', True)
        return self.create_user(email, senha, **campos_extras)

class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Classe de Definição da modelagem do Objeto.
    """
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = GerenciadorUsuario()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'data_nascimento', 'sexo', 'cidade', 'uf']

    def __str__(self):
        return self.email
