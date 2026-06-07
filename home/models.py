from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class HomeInfo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='home_images/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['sort']


class Review(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    home_info = models.ForeignKey(HomeInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['-grade']