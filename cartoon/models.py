from django.db import models

# Create your models here.
class contactMe(models.Model):
    fname=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    phn=models.IntegerField(null=True, blank=True)
    msg=models.CharField(max_length=50)