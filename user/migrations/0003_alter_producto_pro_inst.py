# Generated by Django 3.2.2 on 2021-05-12 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210511_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='pro_inst',
            field=models.CharField(choices=[('Calca', 'Calça'), ('Camisa', 'Camisa'), ('Bermuda', 'Bermuda'), ('Saia', 'Saia'), ('Vestido', 'Vestido')], max_length=9, verbose_name='Tipo:'),
        ),
    ]
