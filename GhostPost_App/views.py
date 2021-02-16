from django.shortcuts import render, redirect

from GhostPost_App.models import GhostPostModel
# from GhostPost_App.forms import GhostPostForm


# Create your views here.
def index_view(request):
    posts = GhostPostModel.objects.all()
    
    return render(request, 'index.html', {
      'posts': posts
    })


def likes_view(request, post_id):
    post = GhostPostModel.objects.filter(id=post_id).first()
    post.likes += 1
    post.save()
    return redirect('/')


def dislikes_view(request, post_id):
    post = GhostPostModel.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.save()
    return redirect('/')