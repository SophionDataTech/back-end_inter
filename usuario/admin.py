from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario

class UsuarioAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'nome', 'cidade', 'uf']
    estrutura_dos_campos = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {
            'fields': ('nome', 'data_nascimento', 'sexo', 'cidade', 'uf')
        }),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_estrutura_dos_campos = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'data_nascimento', 'sexo', 'cidade', 'uf', 'password1', 'password2'),
        }),
    )

admin.site.register(Usuario, UsuarioAdmin)
