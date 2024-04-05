from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')