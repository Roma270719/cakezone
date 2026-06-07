from django.db import models

# Create your models here.
class Chefs(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='chefs_photos', blank=True, null=True)
    experience_years = models.PositiveSmallIntegerField()
    education = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['sort']
