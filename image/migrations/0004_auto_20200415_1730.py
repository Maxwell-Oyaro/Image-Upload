# Generated by Django 3.0.5 on 2020-04-15 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20200415_1714'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WebImage',
            new_name='Post',
        ),
    ]
