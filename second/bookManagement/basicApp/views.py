from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from accounts.models import User
from rest_framework.decorators import api_view
from .models import Repositories, Commit
from .forms import RepositoriesForm, CommitForm

# Create your views here.
class AppIndex(TemplateView):
    template_name = 'appIndex.html'

    
@api_view(['GET'])
def GetAllRepositories(request):
    AllUsers = Repositories.objects.all()
    context = {
        'repositories':AllUsers
    }
    return render(request, "basicApp/repositories.html", context)



from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView

class CreateRepoView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    redirect_field_name = 'basicApp/repository_detail.html'
    form_class = RepositoriesForm
    model = Repositories

class RepoDetailView(DetailView):
    model = Repositories




@api_view(['GET'])
def GetAllCommits(request):
    AllCommits = Commit.objects.all().order_by("-createdDate")
    context = {
        'commits':AllCommits
    }
    return render(request, "basicApp/commits.html", context)

class CreateCommitView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    redirect_field_name = 'basicApp/commit_detail.html'
    form_class = CommitForm
    model = Commit

class CommitDetailView(DetailView):
    model = Commit
