# Generated by Django 3.0.3 on 2020-02-12 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnualObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=100, verbose_name='Objetivo')),
                ('slug', models.SlugField(default='1', verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Objetivo',
                'verbose_name_plural': 'Objetivos',
                'ordering': ['objective'],
            },
        ),
    ]