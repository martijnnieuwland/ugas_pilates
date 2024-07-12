from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
