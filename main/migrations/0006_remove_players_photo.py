# Generated by Django 5.0.8 on 2024-08-07 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='photo',
        ),
    ]
