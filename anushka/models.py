from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class drawing2d3d(models.Model):
    caption = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="img")
    image2 = models.ImageField(upload_to="img", blank=True, null=True)
    image3 = models.ImageField(upload_to="img", blank=True, null=True)
    link = models.URLField(blank=True, validators=[URLValidator])

    def __str__(self):
        return self.caption

class Furnitureandtoys(models.Model):
    caption = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="img_profiles")
    image2 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    image3 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    link = models.URLField(blank=True, validators=[URLValidator])

    def __str__(self):
        return self.caption


class printing3d(models.Model):
    caption = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="img_profiles")
    image2 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    image3 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    link = models.URLField(blank=True, validators=[URLValidator])

    def __str__(self):
        return self.caption


class ProductRendering(models.Model):
    caption = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="img_profiles")
    image2 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    image3 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    link = models.URLField(blank=True, validators=[URLValidator])

    def __str__(self):
        return self.caption


class Lasercutting(models.Model):
    caption = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="img_profiles")
    image2 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    image3 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    link = models.URLField(blank=True, validators=[URLValidator])

    def __str__(self):
        return self.caption

class CNCcutting(models.Model):
    caption = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="img_profiles")
    image2 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    image3 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    link = models.URLField(blank=True, validators=[URLValidator])

    def __str__(self):
        return self.caption

class Sheetmetal(models.Model):
    caption = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="img_profiles")
    image2 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    image3 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    link = models.URLField(blank=True, validators=[URLValidator])

    def __str__(self):
        return self.caption

class Metalstrture(models.Model):
    caption = models.CharField(max_length=70)
    description = models.TextField()
    image1 = models.ImageField(upload_to="img_profiles")
    image2 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    image3 = models.ImageField(upload_to="img_profiles", blank=True, null=True)
    link = models.URLField(blank=True, validators=[URLValidator])

    def __str__(self):
        return self.caption


