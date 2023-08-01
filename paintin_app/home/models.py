from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


class painting(models.Model):
    name=models.CharField(max_length=100)
    discription=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    def __str__(self):
        return self.name
class comment(models.Model):
    painting=models.ForeignKey(painting,on_delete=models.CASCADE,related_name="coments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)



