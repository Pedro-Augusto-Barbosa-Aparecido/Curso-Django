from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.views.generic.base import View

from cadastros.forms import CidadeForm
from cadastros.models import Cidade


class SidiaBaseListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'PROJETO SIDIA'
        return context


class CidadeList(SidiaBaseListView):

    queryset = Cidade.objects.all().order_by('nome')
    context_object_name = 'cidades'
    template_name = 'cadastros/lista_cidades.html'


class CidadeDetail(DetailView):

    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastros/detalhe_cidades.html'


class CidadeDelete(DeleteView):
    context_object_name = 'cidade'
    model = Cidade
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeCreate(CreateView):
    model = Cidade
    # fields = ['nome', 'capital']
    form_class = CidadeForm
    template_name = 'cadastros/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeUpdate(UpdateView, SuccessMessageMixin):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Cadastro atualizado com sucesso!'