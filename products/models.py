from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, null=True)
    display_name = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name