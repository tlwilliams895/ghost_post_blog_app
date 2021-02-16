from django.db import models
from django.utils import timezone

# GhostPost Model - One model to represent both boasts and roasts
"""
boast (BooleanField) - to tell whether it's a boast
roast (BooleanField) - to tell whether it's a roast
post (CharField) - to add the content of the post with character limit: 280 characters
likes (IntegerField) - for up votes
dislikes (IntegerField) - for down votes
date (DateTimeField) - for submission time
"""


# Create your models here.
class GhostPostModel(models.Model):
    text = models.CharField(max_length=280)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
      return f"{self.text}"
