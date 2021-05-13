# Generated by Django 3.2.2 on 2021-05-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_producto_pro_inst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='pro_description',
            field=models.TextField(max_length=255, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='pro_name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='pro_price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço'),
        ),
    ]