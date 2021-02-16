from django import forms
# from GhostPost_App.models import GhostPostModel

# GhostPost Form --
"""
class GhostPostModel(models.Model):
  text = models.CharField(max_length=280)
  likes = models.IntegerField(default=0)
  dislikes = models.IntegerField(default=0)
  created_at = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return f"{self.text}"
"""


# Create your FORMS here.
class GhostPostForm(forms.Form):
    boast = forms.BooleanField()
    roast = forms.BooleanField()
    text = forms.CharField(widget=forms.Textarea)
    likes = forms.IntegerField()
    dislikes = forms.IntegerField()
    created_at = forms.DateTimeField(widget=forms.TimeField)