# Generated by Django 2.0.2 on 2018-11-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20181108_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
    ]