# Generated by Django 3.0.5 on 2020-04-15 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0005_auto_20200415_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='size',
        ),
    ]
