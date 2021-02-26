from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from tickets.forms import NovaSolitacaoForm
from tickets.models import Interacao


class NovaSolicitacao(View):

    def get(self, request):

        form = NovaSolitacaoForm

        return render(request, 'tickets/form.html', {'form': form})

    def post(self, request):

        form = NovaSolitacaoForm(request.POST, request.FILES)

        if form.is_valid():

            obj = form.save(commit=True)
            obj.save()

            interacao = Interacao.objects.create(solicitacao=obj, tipo=Interacao.TIPO_STATUS_CHANGE, descricao='Solicitação aberta com sucesso')
            interacao.send_mail_message()

            return redirect('cidades-list')

        return render(request, 'tickets/form.html', {'form': form})