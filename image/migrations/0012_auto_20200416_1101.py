# Generated by Django 3.0.5 on 2020-04-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0011_auto_20200416_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_width',
            field=models.IntegerField(),
        ),
    ]
