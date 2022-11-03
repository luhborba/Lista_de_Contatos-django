from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView, contatos, contato_novo, contato_editar, contato_remover


urlpatterns = [
    path('', ListaPessoaView.as_view(), name='pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name='pessoa.novo'),
    path('<int:pk>/edit/', PessoaUpdateView.as_view(), name='pessoa.edit'),
    path('<int:pk>/del/', PessoaDeleteView.as_view(), name='pessoa.del'),
    path('<int:pk_pessoa>/contatos/', contatos, name='pessoa.contatos'),
    path('<int:pk_pessoa>/contatos/novo/', contato_novo, name='contato.novo'),
    path('<int:pk_pessoa>/contatos/<int:pk>/edit/', contato_editar, name='contato.edit'),
    path('<int:pk_pessoa>/contatos/<int:pk>/del/', contato_remover, name='contato.del'),
]
