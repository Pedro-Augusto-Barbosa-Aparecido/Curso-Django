from django.contrib import admin

# Register your models here.
from tickets.models import Interacao, Solicitacao, Categoria


class InteracaoInaline(admin.StackedInline):

    model = Interacao

class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nome', 'email', 'assunto', 'status', 'atendente', 'data_solicitacao', 'ultima_atualizacao')
    list_filter = ('categoria', 'status', 'data_solicitacao', 'ultima_atualizacao')
    search_fields = ('nome', 'email', 'assunto')
    inlines = [
        InteracaoInaline
    ]

admin.site.register(Categoria)
admin.site.register(Solicitacao, SolicitacaoAdmin)
