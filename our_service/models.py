from django.db import models
from menu_and_pricing.models import Category

# Create your models here.
class OurService(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.category.name

    class Meta:
        ordering = ['sort']