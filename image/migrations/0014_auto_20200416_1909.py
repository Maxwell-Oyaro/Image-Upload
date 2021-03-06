# Generated by Django 3.0.5 on 2020-04-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0013_remove_post_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(height_field='image_height', upload_to='media/images/', width_field='image_width'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_width',
            field=models.IntegerField(default=0),
        ),
    ]
