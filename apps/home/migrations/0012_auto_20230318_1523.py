# Generated by Django 3.2.16 on 2023-03-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_dado_parcelas_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dado',
            name='deposito',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='dado',
            name='id_vendedor',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name=''),
        ),
    ]
