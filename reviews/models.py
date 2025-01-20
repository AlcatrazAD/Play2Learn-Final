from django.db import models

from django.urls import reverse

# Create your models here.

class Review(models.Model):
    submission = models.TextField(max_length=200)
    
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('reviews:detail', args=[str(self.pk)])
   
    def __str__(self):
        return self.submission