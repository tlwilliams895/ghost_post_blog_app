from django.shortcuts import render, redirect

from GhostPost_App.models import GhostPostModel
from GhostPost_App.forms import GhostPostForm


# Create your views here.
def index_view(request):
    posts = GhostPostModel.objects.order_by('created_at')
    return render(request, 'index.html', {
      'home': 'Ghost Post Home',
      'posts': posts
    })


# UpVotes Detail View
def likes_view(request, post_id):
    post = GhostPostModel.objects.filter(id=post_id).first()
    post.likes += 1
    post.save()
    return redirect('/')


# DownVotes Detail View
def dislikes_view(request, post_id):
    post = GhostPostModel.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.save()
    return redirect('/')


# Sort By Votes Detail View
# Ability to sort content based on vote score
def votes_view(request):
  ...


# Boast View Detail
def boast_view(request):
  ...


# Roast View Detail
def roast_view(request):
  ...

# Page to submit a boast or a roast
def add_post(request):
    if request.method == "POST":
        form = GhostPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPostModel.objects.create(
              is_roast=data['is_roast'],
              text=data['text']
            )

    form = GhostPostForm()
    return render(request, 'post_form.html', {
      'post_form': form
    })
