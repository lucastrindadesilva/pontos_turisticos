from django.db import models
from django.db.models.fields.related import ForeignKey
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

# Create your models here.


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome