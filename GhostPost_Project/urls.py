"""GhostPost_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GhostPost_App import views

urlpatterns = [
    path('', views.index_view, name="home"),
    path('boast/', views.boast_view, name="boast"),
    path('roast/', views.roast_view, name="roast"),
    path('likes/<int:post_id>/', views.likes_view, name="likes"),
    path('dislikes/<int:post_id>/', views.dislikes_view, name="dislikes"),
    path('sort_votes/', views.votes_view, name="votes"),
    path('add_post/', views.add_post, name="add_post"),
    path('update_server/', views.ghostpost_update, name="update"),
    path('admin/', admin.site.urls),
]
