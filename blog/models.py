from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Post(models.Model):
    banner = models.ImageField(null=True, blank=True, upload_to="blog_images/")
    title = models.CharField(max_length=140)
    lead = models.TextField()
    text = tinymce_models.HTMLField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
