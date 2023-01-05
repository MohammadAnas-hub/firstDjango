from django.urls import path
from validators import visa
from . import views

app_name = 'basicApp'

urlpatterns = [
    path("get-all-repositories", views.GetAllRepositories, name="GetAllRepositories"),
    path("create-repository", views.CreateRepoView.as_view(), name="CreateRepoView"),
    path("repositroy-detail/(?P<pk>\d+)", views.RepoDetailView.as_view(), name="RepoDetailView"),
    path("get-all-commits", views.GetAllCommits, name="GetAllCommits"),
    path("create-commit", views.CreateCommitView.as_view(), name="CreateCommitView"),
    path("commit-detail/(?P<pk>\d+)", views.CommitDetailView.as_view(), name="CommitDetailView"),
]