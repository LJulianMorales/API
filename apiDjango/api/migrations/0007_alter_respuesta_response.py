# Generated by Django 3.2.4 on 2023-10-21 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20231020_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='response',
            field=models.TextField(),
        ),
    ]
