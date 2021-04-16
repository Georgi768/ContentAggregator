from django.db import models


# Create your models here.

class Content(models.Model):
    Title = models.CharField(max_length=255)
    Link = models.CharField(max_length=255)
    Image = models.CharField(max_length=255)

    class Meta:
        db_table = 'contents'
