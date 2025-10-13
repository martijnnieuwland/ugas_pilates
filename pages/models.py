from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='instructor_images/', null=True, blank=True)

    def __str__(self):
        return self.name
