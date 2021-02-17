from django import forms
# from GhostPost_App.models import GhostPostModel


# Create your FORMS here.
# Django Resource: https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
class GhostPostForm(forms.Form):
    VOTE_CHOICES = [(True, 'Boast'), (False, 'Roast')]
    is_roast = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=VOTE_CHOICES
    )
    # is_roast = forms.CharField(label="Is This a Roast or Boast?")
    text = forms.CharField(widget=forms.Textarea)
    # likes = forms.IntegerField()
    # dislikes = forms.IntegerField()
    # created_at = forms.DateTimeField(widget=forms.TimeField)