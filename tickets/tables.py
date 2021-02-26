import django_tables2 as table

from tickets.models import Solicitacao


class SolicitacaoTable(table.Table):

    actions = table.TemplateColumn(template_name='tickets/actions.html')

    class Meta:
        model = Solicitacao
        fields = ('actions', 'id', 'categoria', 'nome', 'email', 'assunto', 'status', 'atendente', 'data_solicitacao', 'data_atualizacao')
