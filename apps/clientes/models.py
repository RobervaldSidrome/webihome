from django.db import models

# Data de Criação - 14/02/2019
# Analyst/Developer Robervald Sidrome
# Modelo Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome