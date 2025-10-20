from django.db import models
from django.contrib.auth.models import User

class Pergunta(models.Model):
    NIVEL_CHOICES = [
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
    ]

    texto = models.CharField(max_length=255)
    nivel = models.CharField(max_length=10, choices=NIVEL_CHOICES)
    opcoes = models.JSONField()
    resposta_correta = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.texto} ({self.nivel})"

class Resultado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.pontuacao} pts"
