from django.urls import path
from .views import ListaPessoaView


urlpatterns = [
    path('', ListaPessoaView.as_view(), name='pessoas.index'),
]
