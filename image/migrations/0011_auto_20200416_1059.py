# Generated by Django 3.0.5 on 2020-04-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0010_auto_20200416_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='size',
            field=models.BinaryField(),
        ),
    ]
