# Generated by Django 2.2.5 on 2020-01-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
