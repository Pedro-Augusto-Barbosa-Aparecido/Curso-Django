from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms

from tickets.models import Solicitacao


class NovaSolitacaoForm(forms.ModelForm):

    class Meta:
        model = Solicitacao
        fields = ['categoria', 'nome', 'email', 'assunto', 'descricao', 'arquivo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Dados pessoais',
                'nome',
                'email'
            ),
            Fieldset(
                'Mensagem',
                'categoria',
                'assunto',
                'descricao',
                'arquivo'
            ),
            ButtonHolder(
                Submit('submit', 'Enviar solicitação', css_clas='btn btn-primary')
            )
        )
