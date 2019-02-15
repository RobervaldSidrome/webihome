from django.db import models

# Data de Criação - 14/02/2019
# Analyst/Developer Robervald Sidrome
# Modelo Segmento Profissional

class SegmentoProfissional(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return self.nome