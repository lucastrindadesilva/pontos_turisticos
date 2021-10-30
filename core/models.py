from django.db import models
from atracoes.models import Atracao

# Create your models here.


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)

    def __str__(self) -> str:
        return self.nome