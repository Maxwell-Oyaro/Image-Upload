# Generated by Django 3.0.5 on 2020-04-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20200415_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webimage',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
