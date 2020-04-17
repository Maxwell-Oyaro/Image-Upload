from image.models import Post
from django.forms import ModelForm

#Create form class here
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'cover']
#Create form
form = PostForm()
