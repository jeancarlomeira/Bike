from django.db import models


class Activity(models.Model):
    distance = models.DecimalField('Distância em km', max_digits=5, decimal_places=2)
    date = models.DateField('Data', help_text="No formato dd/mm/aaaa")
    slug = models.SlugField('Identificador', max_length=100, help_text="Preenchido automaticamente, não editar.",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        ordering = ['created']

    def __str__(self):
        return self.slug
