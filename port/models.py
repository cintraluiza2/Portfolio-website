from django.db import models
from django.conf import settings

class Contato(models.Model):
    nome = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=100)
    email = models.EmailField()
    corpo = models.TextField()
    enviado = models.BooleanField()

    def __str__(self):
        return self.assunto
