from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200,null=True,blank=True)
    thumbnail = models.ImageField(null=True, blank = True, upload_to = "images",default="/images/1.jpg")
    body = models.TextField(null=True,blank=True)
    created = models.TimeField(auto_now_add=True)
    activity = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)
    #slug = 
    
    def __str__(self):
        return self.headline
    