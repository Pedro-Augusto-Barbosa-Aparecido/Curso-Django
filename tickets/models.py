from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Categoria(models.Model):

    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ('descricao', )

    def __str__(self):
        return self.descricao

class Solicitacao(models.Model):

    STATUS_NEW = 'new'
    STATUS_ONGOING = 'ongoing'
    STATUS_CLOSED = 'closed'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Novo'),
        (STATUS_ONGOING, 'Em andamento'),
        (STATUS_CLOSED, 'Encerrado'),
        (STATUS_CANCELED, 'Cancelado')
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nome = models.CharField(max_length=128)
    email = models.EmailField(verbose_name='E-mail')
    assunto = models.CharField(max_length=80)
    descricao = models.TextField(verbose_name='Descrição')
    arquivo = models.FileField(upload_to='solicitacoes', null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_NEW)
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name='Data-Solicitação')
    ultima_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data-Atualizaçãp')

    class Meta:
        ordering = ('-ultima_atualizacao', )
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

    def __str__(self):
        return f'TICKET{self.pk:04d}'

    # def save(self, *args, **kwargs):
    #
    #     if self.pk:
    #         pass
    #
    #     super().save(*args, **kwargs)


class Interacao(models.Model):

    TIPO_ASSIGNED = 0
    TIPO_TEAM_RESPONSE = 1
    TIPO_REQUEST_RESPONSE = 2
    TIPO_STATUS_CHANGE = 3

    TIPO_CHOICES = (
        (TIPO_ASSIGNED, 'Assinado para o atendente'),
        (TIPO_TEAM_RESPONSE, 'Resposta do time'),
        (TIPO_REQUEST_RESPONSE, 'Resposta do solicitante'),
        (TIPO_STATUS_CHANGE, 'Mudança de status'),
    )

    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    tipo = models.PositiveSmallIntegerField(choices=TIPO_CHOICES)
    descricao = models.TextField()
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    data_interacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-data_interacao', )
        verbose_name = 'Interação'
        verbose_name_plural = 'Interações'

    def __str__(self):
        return f'{self.pk}'

    def send_mail_message(self):
        pass
