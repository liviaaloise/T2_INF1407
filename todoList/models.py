from django.db import models

# Create your models here.
class Tarefa(models.Model):
    # nickname = models.CharField(max_length=30, help_text="entre com o seu nickname")
    texto = models.CharField(max_length=200, help_text="digite a mensagem")
    prazo = models.DateField(help_text="digite a data da entrega")
    
