# Generated by Django 2.2.4 on 2019-10-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20191027_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='file',
            field=models.FileField(upload_to='archivos/'),
        ),
    ]