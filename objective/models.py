from django.db import models


class AnualObjective(models.Model):
    objective = models.CharField('Objetivo', max_length=100)
    slug = models.SlugField('Identificador', default='1')

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Objetivo'
        verbose_name_plural = 'Objetivos'
        ordering = ['objective']

    def __str__(self):
        return self.objective
