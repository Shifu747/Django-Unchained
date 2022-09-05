from django.db import models
from django.urls import reverse

# Create your models here.
class Cast(models.Model):
    character_name      = models.CharField(max_length=255)
    played_by           = models.CharField(max_length=255)
    description         = models.TextField()
    popular_film        = models.TextField()
    image               = models.ImageField(null=True, blank=True, upload_to ='images/')


    def get_absolute_url(self):
        return reverse('cast_detail', kwargs={'id':self.id})


