from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView, contatos, contato_novo, contato_editar, contato_remover
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaPessoaView.as_view()), name='pessoa.index'),
    path('novo/', login_required(PessoaCreateView.as_view()), name='pessoa.novo'),
    path('<int:pk>/edit/', login_required(PessoaUpdateView.as_view()), name='pessoa.edit'),
    path('<int:pk>/del/', login_required(PessoaDeleteView.as_view()), name='pessoa.del'),
    path('<int:pk_pessoa>/contatos/', login_required(contatos), name='pessoa.contatos'),
    path('<int:pk_pessoa>/contatos/novo/', login_required(contato_novo), name='contato.novo'),
    path('<int:pk_pessoa>/contatos/<int:pk>/edit/', login_required(contato_editar), name='contato.edit'),
    path('<int:pk_pessoa>/contatos/<int:pk>/del/', login_required(contato_remover), name='contato.del'),
]
