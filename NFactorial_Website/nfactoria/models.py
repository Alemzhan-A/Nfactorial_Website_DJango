from django.db import models
from django.contrib.auth.models import User

class Music(models.Model):
    music_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1500)
    author = models.CharField(max_length=1500)
    genre = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='photos')
    song = models.FileField(upload_to='photos')

class Review(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.music.name} by {self.user.username}'

