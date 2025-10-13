from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='instructor_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Pricelist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} Pricelist"


class PricelistItem(models.Model):
    pricelist = models.ForeignKey(Pricelist, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f"{self.name} - €{self.price}"
