from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=300, null=False)
    release_year = models.IntegerField(null=False)
    genre = models.CharField(max_length=100, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='cover_images')
        
    def __str__(self) -> str:
        return self.title
        
        