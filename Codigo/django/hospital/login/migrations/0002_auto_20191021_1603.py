# Generated by Django 2.2.5 on 2019-10-21 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_personales',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='datos_personales',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
