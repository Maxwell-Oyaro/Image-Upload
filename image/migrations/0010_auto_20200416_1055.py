# Generated by Django 3.0.5 on 2020-04-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0009_post_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(height_field='image_height', upload_to='images/', width_field='image_width'),
        ),
    ]
