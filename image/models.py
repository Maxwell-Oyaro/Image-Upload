from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=40)
    cover = models.ImageField(upload_to='media/images/', height_field='image_height', width_field='image_width', max_length=1000)
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)


    def __str__(self):
        return self.name
