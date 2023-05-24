from django.db import models

class Myimages(models.Model):
  id = models.AutoField(primary_key=True)
  text = models.CharField(max_length=500)
  imgurl = models.CharField(max_length=500)
  date = models.DateField()


  
