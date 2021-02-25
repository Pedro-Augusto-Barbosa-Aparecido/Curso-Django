from rest_framework import serializers

from cadastros.models import Cidade


class CidadeSerializer(serializers.ModelSerializer):

    estado_nome = serializers.ReadOnlyField(source='estado.nome')
    # pais_nome = serializers.ReadOnlyField(source='estado.pais.nome')
    # estado = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Cidade
        fields = ['id', 'estado', 'estado_nome', 'nome', 'capital', 'descricao']