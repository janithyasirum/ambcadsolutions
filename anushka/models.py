from django.db import models


# Create your models here.
class drawing2d3d(models.Model):
    caption = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="img")

    def __str__(self):
        return self.caption


class printing3d(models.Model):
    caption = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="img_profiles")

    def __str__(self):
        return self.caption


class ProductRendering(models.Model):
    caption = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="img_profiles")

    def __str__(self):
        return self.caption


class Lasercutting(models.Model):
    caption = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="img_profiles")

    def __str__(self):
        return self.caption

class CNCcutting(models.Model):
    caption = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="img_profiles")

    def __str__(self):
        return self.caption

# class Laserandplasma(models.Model):
#     caption = models.CharField(max_length=300)
#     description = models.TextField()
#     image = models.ImageField(upload_to="img_profiles")
#
#     def __str__(self):
#         return self.caption
