from django.db import models

# Create your models here.
class phoneSpecs(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    capacity = models.CharField(max_length=30)
    price = models.CharField(max_length=50)
    publication_date = models.DateField()
    website = models.URLField()

    def __str__(self):
        return self.name