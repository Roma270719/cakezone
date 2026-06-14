from django.db import models

# Create your models here.
class MessageFromCustomer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    is_protected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}-{self.subject}'

    class Meta:
        ordering = ['created_at']

class ContactUs(models.Model):
    address = models.TextField()
    photo = models.ImageField(upload_to='contact_us_photos/', blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.address

    class Meta:
        ordering = ['sort']
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

