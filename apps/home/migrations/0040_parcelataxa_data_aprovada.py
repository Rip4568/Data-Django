# Generated by Django 3.2.16 on 2023-05-23 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20230522_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcelataxa',
            name='data_aprovada',
            field=models.DateField(blank=True, null=True, verbose_name=''),
        ),
    ]
