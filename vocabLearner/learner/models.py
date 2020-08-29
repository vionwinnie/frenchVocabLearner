# from django.db import models
from firebase_orm import models
# Create your models here.

class title(models.Model):
    title = models.TextField()
    
    def __str__(self):
        return self.title

   