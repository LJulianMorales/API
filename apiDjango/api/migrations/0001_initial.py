# Generated by Django 3.2.4 on 2023-10-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]