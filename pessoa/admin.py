from django.contrib import admin
from .models import Pessoa, Contato

# Register your models here.

@admin.action(description='Ativar Selecionados')
def ativa_todos(modeladmin, request, queryset):
    queryset.update(ativa=True)

@admin.action(description='Desativar Selecionados')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)

class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa'
    ]
    list_filter = ['ativa','data_nascimento']
    search_fields = [
        'nome_completo',
    ]
    actions = [ativa_todos,desativar_todos]

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)