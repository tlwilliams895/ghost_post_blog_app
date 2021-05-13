from django.shortcuts import render, reverse, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git

from GhostPost_App.models import GhostPostModel
from GhostPost_App.forms import GhostPostForm


# Create your views here.
def index_view(request):
    posts = GhostPostModel.objects.order_by('-created_at')
    return render(request, 'index.html', {
      'home': 'Ghost Post Home',
      'votes': 'Is this a Boast or Roast?',
      'posts': posts
    })


# UpVotes/Likes Detail View --
# When clicked, the button affects the UpVote numbers
# on the relevant post appropriately
def likes_view(request, post_id):
    post = GhostPostModel.objects.filter(id=post_id).first()
    post.likes += 1
    post.save()
    # Resource: StackOverflow
    # https://stackoverflow.com/questions/14010177/how-do-i-use-request-meta-gethttp-referer-within-template
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# DownVotes/Dislikes Detail View --
# When clicked, the button affects the DownVote numbers
# on the relevant post appropriately
def dislikes_view(request, post_id):
    post = GhostPostModel.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Boast View Detail
# Filters the content by boasts and sorted by time submitted
def boast_view(request):
    boast = GhostPostModel.objects.filter(is_roast=True).order_by('-created_at')

    return render(request, 'boast.html', {
      'boast_view': 'Ghost Post - Boasts',
      'boast': boast
    })


# Roast View Detail
# Filters the content by roasts and sorted by time submitted
def roast_view(request):
    roast = GhostPostModel.objects.filter(is_roast=False).order_by('-created_at')

    return render(request, 'roast.html', {
      'roast_view': 'Ghost Post - Roasts',
      'roast': roast
    })


# Sort By Votes Detail View
# Ability to sort content based on vote score; Use key lambda function
def votes_view(request):
    votes = sorted(GhostPostModel.objects.all(), key=lambda votes: votes.vote_score())[::-1]

    return render(request, 'votes.html', {
      'sort_votes': 'GhostPost - Sort By Votes',
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
            return HttpResponseRedirect(reverse('home'))

    form = GhostPostForm()
    return render(request, 'post_form.html', {
      'post_form': form
    })


# Deploy Server Function View
# This view function will receive GitHub updates and update the code on the server.
@csrf_exempt
def ghostpost_update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("test.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
