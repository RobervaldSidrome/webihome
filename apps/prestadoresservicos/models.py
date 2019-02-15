from django.db import models

# Data de Criação - 14/02/2019
# Analyst/Developer Robervald Sidrome
# Modelo Prestador de Servico
class PrestadoreServico(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Prestador de Serviço')