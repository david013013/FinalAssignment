from django.db import models

# Create your models here.
class PhotoFeed(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200,null=True)
    photo = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.title
