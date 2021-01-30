from django.db import models
# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=128, null=True)
    display_name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Device(models.Model):
    name = models.CharField(max_length=128, null=True)
    display_name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    device = models.ForeignKey(
        'Device', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.CharField(max_length=254)
    model_name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    stock = models.BooleanField()
    reccomended = models.BooleanField()
    description = models.TextField()
    os = models.CharField(max_length=1020)
    cpu = models.CharField(max_length=1020)
    gpu = models.CharField(max_length=1020)
    ram = models.CharField(max_length=1020)
    storage = models.CharField(max_length=1020)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.model_name
