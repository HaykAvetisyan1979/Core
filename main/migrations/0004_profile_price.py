# Generated by Django 5.0.8 on 2024-08-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_profile_options_alter_profile_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
