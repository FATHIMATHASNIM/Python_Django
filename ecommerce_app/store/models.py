from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.title







# from django.db import models

# # Create your models here.

# from django.db import models

# class Product(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image_url = models.URLField(max_length=200)

#     def __str__(self):
#         return self.title


