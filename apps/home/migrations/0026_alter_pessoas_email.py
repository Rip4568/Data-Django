# Generated by Django 4.1.3 on 2023-04-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_parcelataxa_aprovada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
