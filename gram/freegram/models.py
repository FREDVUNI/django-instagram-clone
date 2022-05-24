from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    username =models.CharField(max_length=50)
    email =models.CharField(max_length=80)
    slug =models.CharField(max_length=10)
    image =models.FileField()

    def get_absolute_url(self):
        return reverse("freegram:index")

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.CharField(max_length=50)
    slug =models.CharField(max_length=10)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse("freegram:details",kwargs={"slug":self.slug})

    def __str__(self):
        return self.caption