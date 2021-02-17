from django.db import models
from django.utils import timezone

# GhostPost Model - One model to represent both boasts and roasts
"""
is_roast (BooleanField) - to tell whether it's a roast or a boast
text (CharField) - to add the content of the post with character limit: 280 characters
likes (IntegerField) - for up votes
dislikes (IntegerField) - for down votes
created_at (DateTimeField) - for submission time
secret_key (CharField)
"""


# Create your models here.
class GhostPostModel(models.Model):
    is_roast = models.BooleanField()
    text = models.CharField(max_length=280)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    # secret_key = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.text} | {self.created_at}"

    def vote_score(self):
        return self.likes - self.dislikes
