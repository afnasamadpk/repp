from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length = 60)
    image = models.ImageField(upload_to='images')
    users = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='post')
    class Meta:
        unique_together = ['user','post']
    