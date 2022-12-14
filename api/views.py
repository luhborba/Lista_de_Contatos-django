from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import PessoaSerializer
from pessoa.models import Pessoa
# Create your views here.

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all().order_by('nome_completo')
    serializer_class = PessoaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pessoa = super().get_queryset()
        pessoa = pessoa.filter(usuario=self.request.user)
        return pessoa