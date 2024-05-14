# Generated by Django 5.0.3 on 2024-04-04 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default='Tamil Nadu', max_length=64),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
    ]