from django.shortcuts import render, redirect

from GhostPost_App.models import GhostPostModel
from GhostPost_App.forms import GhostPostForm


# Create your views here.
def index_view(request):
    posts = GhostPostModel.objects.order_by('-created_at')
    return render(request, 'index.html', {
      'home': 'Ghost Post Home',
      'posts': posts
    })


# UpVotes/Likes Detail View --
# When clicked, the button affects the UpVote numbers
# on the relevant post appropriately
def likes_view(request, post_id):
    post = GhostPostModel.objects.filter(id=post_id).first()
    post.likes += 1
    post.save()
    return redirect('/')


# DownVotes/Dislikes Detail View --
# When clicked, the button affects the DownVote numbers
# on the relevant post appropriately
def dislikes_view(request, post_id):
    post = GhostPostModel.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.save()
    return redirect('/')


# Boast View Detail
# Filters the content by boasts and sorted by time submitted
def boast_view(request):
    boast = GhostPostModel.objects.order_by('-created_at')

    return render(request, 'boast.html', {
      'boast_view': 'Ghost Post - Boasts',
      'boast': boast
    })


# Roast View Detail
# Filters the content by roasts and sorted by time submitted
def roast_view(request):
    roast = GhostPostModel.objects.order_by('-created_at')

    return render(request, 'roast.html', {
      'roast_view': 'Ghost Post - Roasts',
      'roast': roast
    })


# Sort By Votes Detail View
# Ability to sort content based on vote score
def votes_view(request):
    votes = GhostPostModel.objects.order_by('-created_at')
    
    return render(request, 'votes.html', {
      'sort_votes': 'Sort By Votes',
      'votes': votes
    })


# Create Post Detail View
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
