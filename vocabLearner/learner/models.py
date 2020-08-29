# from django.db import models
from firebase_orm import models
# Create your models here.

class title(models.Model):
    title = models.TextField()
    pub_date = models.DateTimeField('date published') 

    def __str__(self):
        return self.title

    def was_published(self):
         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)