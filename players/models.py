from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

# Create your models here.
class Players(models.Model):
    player_Name = models.CharField(max_length=64)
    position = models.TextField(max_length=64)
    age = models.CharField(max_length=64)
    team = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.player_Name
