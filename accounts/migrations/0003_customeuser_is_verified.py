# Generated by Django 4.0 on 2024-02-24 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customeuser_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]