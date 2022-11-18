from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.categoria


class Pergunta(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    pergunta = models.CharField(max_length=100, unique=True)

    escolha1 = models.CharField(max_length=50)
    escolha2 = models.CharField(max_length=50)
    escolha3 = models.CharField(max_length=50)

    resposta = models.CharField(max_length=50)

    def __str__(self):
        return self.pergunta
