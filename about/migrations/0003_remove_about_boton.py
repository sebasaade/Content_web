# Generated by Django 2.0.2 on 2018-11-03 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20181103_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='boton',
        ),
    ]