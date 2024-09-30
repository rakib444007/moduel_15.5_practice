from django.db import models
from musician.models import Musician
# Create your models here.


class Album(models.Model):
    AlbumName = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    ReleaseDate  = models.DateField(auto_now_add=True)
    ch = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]
    rating= models.PositiveSmallIntegerField(choices=ch)

    def __str__(self):
        return self.AlbumName

 
