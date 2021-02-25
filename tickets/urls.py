from django.urls import include, path

from tickets.views import NovaSolicitacao

urlpatterns = [
    path('tickets/', NovaSolicitacao.as_view(), name='cidades-list'),
]